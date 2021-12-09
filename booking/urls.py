from django.contrib import admin
from django.urls import path, include

from custom_users import urls as users

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(users))
]
