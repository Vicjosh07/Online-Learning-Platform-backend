from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.decorators import role_required
from dashboard.models import Course, CourseTopic, UserCourse
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views.decorators.csrf import csrf_exempt
from accounts.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist


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


@role_required('LECTURER')
def profile(request):
    levels = Course.get_level_choices()

    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Create a UserProfile if it doesn't exist
        user_profile = UserProfile.objects.create(user=request.user, matric="", phonenumber="", description="")

    context = {
        'levels': levels,
        'user_profile': user_profile,
    }

    return render(request, 'sections/profile.html', context)

@role_required('LECTURER')
@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        try:
            # Basic validation
            if 'thumbnail' not in request.FILES:
                return JsonResponse({
                    'success': False,
                    'error': 'Thumbnail is required'
                }, status=400)

            print("Received files:", request.FILES)
            print("Received data:", request.POST)
            # Create course with direct file assignment
            course = Course(
                title=request.POST['title'],
                document_link=request.POST['document_link'],
                level=request.POST['level'],
                department=request.POST['department'],
                description=request.POST['description'],
                lecturer=request.user,
                thumbnail=request.FILES['thumbnail']  # Assign directly
            )
            course.save()

            return JsonResponse({
                'success': True,
                'course_id': course.id,
                'course_title': course.title
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)


    return JsonResponse({'success': False}, status=405)

def add_topic(request):
    if request.method == 'POST':
        try:
            course = Course.objects.get(id=request.POST['course_id'])
            topic = CourseTopic(
                course=course,
                title=request.POST['topic_title'],
                content=request.POST['topic_content'],
                order=CourseTopic.objects.filter(course=course).count() + 1
            )
            topic.save()
            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            }, status=400)
    return JsonResponse({'success': False}, status=405)

@role_required('LECTURER')
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id, lecturer=request.user)
    course.delete()
    # Add a success message
    messages.success(request, "Course removed successfully!")

    # Redirect back to the user's courses page
    return redirect('upload_course')
  