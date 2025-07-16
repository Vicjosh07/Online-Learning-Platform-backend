from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.decorators import role_required
from .models import Course, UserCourse
from accounts.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile



@login_required
@role_required('STUDENT', 'VISITOR')
def dashb(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')  # Redirect to login page if not authenticated
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Create a UserProfile if it doesn't exist
        user_profile = UserProfile.objects.create(user=request.user, matric="", phonenumber="", description="")

    all_courses = Course.objects.all()
    personalized_courses = user_profile.get_personalized_courses()

    context = {
        'all_courses': all_courses,
        'personalized_courses': personalized_courses,
    }
    return render(request, 'dashboard/courses.html', context)


@login_required
@role_required('STUDENT', 'VISITOR')
def add_course(request, course_id):
    # Get the course and user profile
    course = get_object_or_404(Course, id=course_id)
    user_profile = UserProfile.objects.get(user=request.user)

    # Check if the course is already added
    if not UserCourse.objects.filter(user_profile=user_profile, course=course).exists():
        UserCourse.objects.create(user_profile=user_profile, course=course)
        messages.success(request, f"Course '{course.title}' has been added to your dashboard!")
    else:
        messages.warning(request, f"Course '{course.title}' is already in your dashboard.")

    return redirect('dashb')


@login_required
def remove_course(request, user_course_id):
    # Get the UserCourse object or return 404 if not found
    user_course = get_object_or_404(UserCourse, id=user_course_id, user_profile__user=request.user)

    # Delete the UserCourse object
    user_course.delete()

    # Add a success message
    messages.success(request, "Course removed successfully!")

    # Redirect back to the user's courses page
    return redirect('dashb')


@login_required
def profile(request):
    # Fetch the UserProfile for the logged-in user
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except ObjectDoesNotExist:
        # Create a UserProfile if it doesn't exist
        user_profile = UserProfile.objects.create(user=request.user, matric="", phonenumber="", description="")

    # Pass the user_profile to the template
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'dashboard/user-profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        user_profile = UserProfile.objects.get(user=request.user)

        # Update text fields
        user_profile.occupation = request.POST.get('occupation', '')
        user_profile.phonenumber = request.POST.get('phonenumber', '')
        user_profile.description = request.POST.get('description', '')
        user_profile.linkedin = request.POST.get('linkedin', '')
        user_profile.facebook = request.POST.get('facebook', '')

        # Handle profile picture upload
        if 'profile_pic' in request.FILES:
            img = Image.open(request.FILES['profile_pic'])

            # Resize image to 200x200
            try:
                if img.height > 200 or img.width > 200:
                    output_size = (200, 200)
                    img.thumbnail(output_size)

                    # Convert to BytesIO
                    output = BytesIO()
                    img.save(output, format='JPEG', quality=90)
                    output.seek(0)

                    # Create new InMemoryUploadedFile
                    user_profile.profile_pic = InMemoryUploadedFile(
                        output,
                        'ImageField',
                        f"{request.FILES['profile_pic'].name}",
                        'image/jpeg',
                        output.tell(),
                        None
                    )
                else:
                    user_profile.profile_pic = request.FILES['profile_pic']

            except:
                messages.warning(request, f"The image exceeds approparite dimension.")
            

        user_profile.save()
        messages.success(request, 'Profile updated successfully!')

        if user_profile.role == 'LECTURER':
            return redirect('upload_course')
        return redirect('dashb')