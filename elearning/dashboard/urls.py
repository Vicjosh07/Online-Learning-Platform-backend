from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashb, name='dashb'),  # This matches the 'dashb' name used in redirects
    path('add-course/<int:course_id>/', views.add_course, name='add_course'),
    path('remove-course/<int:user_course_id>/', views.remove_course, name='remove_course'),
    path('profile/', views.profile, name='profile'),
    path('update-profile/', views.update_profile, name='update_profile'),
]