from django.db import models
from django.conf import settings

class Course(models.Model):
    LEVEL_CHOICES = [
        ('100', '100 Level'),
        ('200', '200 Level'),
        ('300', '300 Level'),
        ('400', '400 Level'),
        ('500', '500 Level'),
    ]

    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    title = models.CharField(max_length=200)
    lecturer = models.CharField(max_length=100)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    department = models.CharField(max_length=100)
    description = models.TextField()
    document_link = models.URLField(blank=True, null=True)  # Link to course material

    def __str__(self):
        return self.title

class UserCourse(models.Model):
    user_profile = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'course')  # Ensure a user can't add the same course twice

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.course.title}"