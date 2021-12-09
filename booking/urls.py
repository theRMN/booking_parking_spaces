from django.contrib import admin
from django.urls import path, include

from custom_users import urls as users_urls
from api import urls as api_urls
from accounts import urls as accounts_urls

urlpatterns = [
    path('', include(accounts_urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include(users_urls)),
    path('api/v1/', include(api_urls))
]
