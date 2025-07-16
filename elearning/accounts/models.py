# accounts/models.py
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User
import os
from django.dispatch import receiver
from django.db.models.signals import post_save


def user_profile_pic_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/profile_pics/user_<id>/<filename>
    return f'profile_pics/user_{instance.user.id}/{filename}'


class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('STUDENT', 'Student'),
        ('VISITOR', 'Visitor'),
        ('LECTURER', 'Lecturer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to=user_profile_pic_path,
        default='profile_pics/default.png',  # Add this default image to your media folder
        blank=True
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
    matric = models.CharField(max_length=50, default=" ")
    phonenumber = models.CharField(max_length=15, default=" ")
    description = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=255, blank=True, null=False, default="")
    facebook = models.CharField(max_length=255, blank=True, null=False, default="")
    occupation = models.CharField(max_length=255, blank=True, null=False, default="")

    def is_lecturer(self):
        return self.role == 'LECTURER'
    
    def is_student(self):
        return self.role == 'STUDENT'


    def get_personalized_courses(self):
        from dashboard.models import UserCourse
        return UserCourse.objects.filter(user_profile=self).select_related('course')

    def __str__(self):
        # Display full name if available, fall back to username
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name
