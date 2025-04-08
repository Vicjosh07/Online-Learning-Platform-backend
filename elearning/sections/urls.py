from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('courses/', views.all_courses, name='all_courses'),
    path('blog_details/', views.blog_details, name='blog_details'),

]
