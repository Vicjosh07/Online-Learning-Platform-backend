from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, UserCourse
from accounts.models import UserProfile
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required


def dashb(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')  # Redirect to login page if not authenticated
    return render(request, 'dashboard/index.html')

@login_required
def course(request):
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

    return redirect('course')


@login_required
def remove_course(request, user_course_id):
    # Get the UserCourse object or return 404 if not found
    user_course = get_object_or_404(UserCourse, id=user_course_id, user_profile__user=request.user)

    # Delete the UserCourse object
    user_course.delete()

    # Add a success message
    messages.success(request, "Course removed successfully!")

    # Redirect back to the user's courses page
    return redirect('course')


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
        # Fetch the UserProfile for the logged-in user
        user_profile = UserProfile.objects.get(user=request.user)

        # Update the fields from the form data
        user_profile.occupation = request.POST.get('occupation', '')
        user_profile.phonenumber = request.POST.get('phonenumber', '')
        user_profile.description = request.POST.get('description', '')
        user_profile.linkedin = request.POST.get('linkedin', '')
        user_profile.facebook = request.POST.get('facebook', '')

        # Save the changes
        user_profile.user.save()
        user_profile.save()

        messages.success(request, 'Profile updated successfully!')
        return redirect('course')

    return redirect('profile')