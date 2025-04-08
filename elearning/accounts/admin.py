from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile

# Unregister the default User admin
admin.site.unregister(User)

# Create an inline admin descriptor for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'User Profile'
    fields = ('matric', 'phonenumber', 'description')  # Ensure 'description' is included

# Define a new User admin
class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_matric', 'get_phonenumber', 'get_description')  # Add 'get_description'
    search_fields = ('username', 'email', 'first_name', 'last_name')

    def get_matric(self, obj):
        return obj.userprofile.matric if hasattr(obj, 'userprofile') else 'N/A'
    get_matric.short_description = 'Matric Number'

    def get_phonenumber(self, obj):
        return obj.userprofile.phonenumber if hasattr(obj, 'userprofile') else 'N/A'
    get_phonenumber.short_description = 'Phone Number'

    def get_description(self, obj):
        return obj.userprofile.description if hasattr(obj, 'userprofile') else 'N/A'
    get_description.short_description = 'Description'  # Column header

# Register the User model with the custom admin
admin.site.register(User, CustomUserAdmin)