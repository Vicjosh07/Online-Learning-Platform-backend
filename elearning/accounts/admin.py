# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fields = ('role', 'matric', 'phonenumber', 'description', 'linkedin', 'facebook', 'occupation')
    filter_horizontal = ()
    readonly_fields = ()

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role', 'get_matric', 'get_phonenumber')
    list_filter = ('userprofile__role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'userprofile__matric')
    
    def get_role(self, obj):
        if hasattr(obj, 'userprofile'):
            return obj.userprofile.get_role_display()
        return 'N/A'
    get_role.short_description = 'Role'
    
    def get_matric(self, obj):
        return obj.userprofile.matric if hasattr(obj, 'userprofile') else 'N/A'
    get_matric.short_description = 'Matric Number'
    
    def get_phonenumber(self, obj):
        return obj.userprofile.phonenumber if hasattr(obj, 'userprofile') else 'N/A'
    get_phonenumber.short_description = 'Phone Number'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('userprofile')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)