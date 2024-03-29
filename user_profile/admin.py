from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from user_profile.models import User, Candidate, ContactMethod, WorkType, WorkCategory, Country, Employer


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    ordering = ('email', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser',
        ),
            'classes': ('collapse',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    # fields = ('first_name', 'last_name', 'email', 'password', 'role', 'is_staff', 'is_active', 'is_superuser',
    #           'groups', 'user_permissions')
    # readonly_fields = ('password',)


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass


@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    pass


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkCategory)
class WorkCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactMethod)
class ContactMethodAdmin(admin.ModelAdmin):
    pass
