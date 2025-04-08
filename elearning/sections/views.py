from django.shortcuts import render
from dashboard.models import Course

# Create your views here.
def index(request):
    # Fetch the top 3 most recent courses
    recent_courses = Course.objects.all().order_by('-id')[:5]  # Assuming 'id' is auto-incremented

    context = {
        'recent_courses': recent_courses,  # Pass the top 3 courses to the template
    }
    return render(request, 'sections/index.html', context)

def about(request):
    return render(request, 'sections/about.html')

def faq(request):
    return render(request, 'sections/faq.html')
def contact(request):
    return render(request, 'sections/contact.html')

def blog(request):
    return render(request, 'sections/blog-standard-sidebar.html')

def all_courses(request):
    # Fetch all courses ordered by date added (most recent first)
    all_courses = Course.objects.all().order_by('-id')  # Assuming 'id' is auto-incremented
    # Fetch the top 3 most recent courses
    recent_courses = all_courses[:3]

    context = {
        'all_courses': all_courses,
        'recent_courses': recent_courses,  # Pass the top 3 courses to the template
    }
    return render(request, 'sections/courses.html', context)

def blog_details(request):
    return render(request, 'sections/blog-details.html')




