from django.http import HttpResponseForbidden
from functools import wraps
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile


def role_required(*allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('user_login')

            try:
                profile = request.user.userprofile
                if profile.role not in allowed_roles:
                    return HttpResponseForbidden("You don't have permission to access this page")
            except UserProfile.DoesNotExist:
                return HttpResponseForbidden("User profile missing")

            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator