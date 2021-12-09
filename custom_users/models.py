from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE_CHOICES = (
    ('manager', 'Менеджер'),
    ('employee', 'Работник'),
)


class CustomUser(AbstractUser):
    type = models.CharField(verbose_name='Тип пользователя', choices=USER_TYPE_CHOICES, max_length=8)
