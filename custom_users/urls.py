from django.urls import path

from custom_users import views

urlpatterns = [
    path('user/login/', views.LoginAccount.as_view(), name='user-login')
]
