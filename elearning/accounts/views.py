from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile

def user_register(request):
    if request.method == "POST":
        # Extract form data
        get_username = request.POST.get("username")
        get_email = request.POST.get("email")
        get_password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        get_matric = request.POST.get("matric")
        get_phonenumber = request.POST.get("phonenumber")
        get_description = request.POST.get("description")

        # Check if email is already registered
        if User.objects.filter(email=get_email).exists():
            messages.warning(request, "Email already exists. Please use a different email.")
            return redirect('user_register')

        # Check if username is already taken
        if User.objects.filter(username=get_username).exists():
            messages.warning(request, "Username already taken. Please choose a different username.")
            return redirect('user_register')

        # Create user
        myuser = User.objects.create_user(username=get_username,
                                          email=get_email,
                                          password=get_password,
                                          first_name=first_name,
                                          last_name=last_name
                                          )
        myuser.save()

        # Create or get UserProfile instance
        UserProfile.objects.get_or_create(
            user=myuser,
            defaults={
                'matric': get_matric,
                'phonenumber': get_phonenumber,
                'description': get_description,
                'first_name': first_name,
                'last_name' : last_name,
            }
        )

        # Authenticate and log in user
        user = authenticate(request, username=get_username, password=get_password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully registered and logged in!")
            return redirect('dashb')  # Redirect to dashboard

    return render(request, "accounts/register.html")

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Find the user by email
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('dashb')  # Redirect to dashboard
            else:
                messages.error(request, "Invalid credentials. Please try again.")
        except User.DoesNotExist:
            messages.error(request, "User does not exist. Please register first.")

    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('index')