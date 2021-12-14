from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('type',)
    UserAdmin.fieldsets += ('Custom fields set', {'fields': ('type',)}),
