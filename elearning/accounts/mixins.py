# accounts/mixins.py
from django.core.exceptions import PermissionDenied
from .models import UserProfile  # Import the UserProfile model

class RoleRequiredMixin:
    allowed_roles = []
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise PermissionDenied
        try:
            profile = request.user.userprofile
            if profile.role not in self.allowed_roles:
                raise PermissionDenied
        except UserProfile.DoesNotExist:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)