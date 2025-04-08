from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matric = models.CharField(max_length=50, default=" ")
    phonenumber = models.CharField(max_length=15, default=" ")
    description = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=255, blank=True, null=False, default="")
    facebook = models.CharField(max_length=255, blank=True, null=False, default="")
    occupation = models.CharField(max_length=255, blank=True, null=False, default="")

    def __str__(self):
        return f"{self.user.username}'s Profile"


    def get_personalized_courses(self):
        from dashboard.models import UserCourse
        return UserCourse.objects.filter(user_profile=self).select_related('course')