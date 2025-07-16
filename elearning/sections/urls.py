from django.urls import path

from accounts.decorators import role_required
from .views import profile
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('courses/', views.all_courses, name='all_courses'),
    path('blog_details/', views.blog_details, name='blog_details'),
    path('profile/', role_required('LECTURER')(profile), name='upload_course'),
    path('add-topic/', views.add_topic, name='add_topic'),
    path('create-course/', views.create_course, name='create_course'),
path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),

]
