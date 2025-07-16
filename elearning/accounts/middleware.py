# accounts/middleware.py
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

from accounts.models import UserProfile


class RoleRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            try:
                profile = request.user.userprofile
                if profile.role == 'LECTURER' and request.path.startswith('/dashboard'):
                    return redirect('upload_course')
                elif profile.role in ['STUDENT', 'VISITOR'] and request.path.startswith('/profile'):
                    return redirect('dashb')
            except UserProfile.DoesNotExist:
                pass

        return response