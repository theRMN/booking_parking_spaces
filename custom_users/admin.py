from django.contrib import admin

from custom_users.models import CustomUser


@admin.register(CustomUser)
class StockProductAdmin(admin.ModelAdmin):
    ...
