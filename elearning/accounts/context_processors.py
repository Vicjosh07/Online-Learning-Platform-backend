from .models import UserProfile

def user_role(request):
    context = {}
    if request.user.is_authenticated:
        try:
            profile = request.user.userprofile
            context.update({
                'user_role': profile.role,
                'is_student': profile.role == 'STUDENT',
                'is_lecturer': profile.role == 'LECTURER',
                'is_visitor': profile.role == 'VISITOR',
                'is_admin': profile.role == 'ADMIN'
            })
        except UserProfile.DoesNotExist:
            pass
    return context