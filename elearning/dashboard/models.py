from django.db import models
from django.conf import settings

class Course(models.Model):
    LEVEL_CHOICES = [
        ('100', '100 Level'),
        ('200', '200 Level'),
        ('300', '300 Level'),
        ('400', '400 Level'),
        ('500', '500 Level'),
        ('600', '600 Level'),
    ]

    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    title = models.CharField(max_length=200)
    lecturer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'userprofile__role': 'LECTURER'},
        related_name='courses_taught'
    )
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    department = models.CharField(max_length=100)
    description = models.TextField()
    document_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_level_choices(cls):
        return cls.LEVEL_CHOICES


class CourseTopic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class UserCourse(models.Model):
    user_profile = models.ForeignKey('accounts.UserProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_profile', 'course')  # Ensure a user can't add the same course twice

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.course.title}"