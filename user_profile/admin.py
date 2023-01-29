from django.contrib import admin

from user_profile.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'email', 'password', 'role', 'is_staff', 'is_active', 'is_superuser',
              'groups', 'user_permissions')
