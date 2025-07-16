from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth import authenticate, login
from django.db import transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile


def user_register(request):
    if request.method == "POST":

        form_data = {
            'username': request.POST.get("username"),
            'email': request.POST.get("email"),
            'password': request.POST.get("password"),
            'first_name': request.POST.get("first_name"),
            'last_name': request.POST.get("last_name"),
            'matric': request.POST.get("matric"),
            'phonenumber': request.POST.get("phonenumber"),
            'description': request.POST.get("description"),
            'role': request.POST.get("role", "STUDENT")
        }

        # Validation checks
        if User.objects.filter(email=form_data['email']).exists():
            messages.error(request, "Email already exists")
            return render(request, "accounts/register.html", {'form_data': form_data})

        if User.objects.filter(username=form_data['username']).exists():
            messages.error(request, "Username already taken")
            return render(request, "accounts/register.html", {'form_data': form_data})

        try:
            with transaction.atomic():
                # Create user (don't login yet)
                user = User.objects.create_user(
                    username=form_data['username'],
                    email=form_data['email'],
                    password=form_data['password'],
                    first_name=form_data['first_name'],
                    last_name=form_data['last_name']
                )

                # Create profile
                UserProfile.objects.create(
                    user=user,
                    matric=form_data['matric'],
                    phonenumber=form_data['phonenumber'],
                    description=form_data['description'],
                    role=form_data['role']
                )

                # Authenticate and login in a separate step
                authenticated_user = authenticate(
                    request,
                    username=form_data['username'],
                    password=form_data['password']
                )

                if authenticated_user is not None:
                    login(request, authenticated_user)
                    messages.success(request, "Registration successful!")

                    # Role-based redirect
                    if form_data['role'] == 'LECTURER':
                        return redirect('upload_course')
                    return redirect('dashb')
                else:
                    messages.error(request, "Authentication failed after registration")
                    return redirect('user_register')

        except Exception as e:
            messages.error(request, f"Registration failed: {str(e)}")
            return redirect('user_register')

    # GET request
    return render(request, "accounts/register.html", {
        'role_choices': [
            ('STUDENT', 'Student'),
            ('VISITOR', 'Visitor'),
            ('LECTURER', 'Lecturer')
        ]
    })

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
            user = authenticate(username=user.username, password=password)

            if user is not None:
                login(request, user)
                profile = user.userprofile  # This will raise exception if profile doesn't exist



                # Role-based redirect
                if profile.role == 'LECTURER':
                    return redirect('upload_course')
                return redirect('dashb')  # For visitors

            messages.error(request, "Invalid credentials")
        except User.DoesNotExist:
            messages.error(request, "User not found")
        except UserProfile.DoesNotExist:
            messages.error(request, "User profile missing - please contact admin")
            return redirect('index')

    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('index')