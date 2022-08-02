from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authnapp.models import CustomUser



@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'gender',
                    'birth_date',
                )
            }
        )
    )

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'gender',
                    'birth_date',
                )
            }
        )
    )