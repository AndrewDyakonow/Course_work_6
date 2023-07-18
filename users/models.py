from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null':True}


class Users(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Почта')
    is_activated = models.BooleanField(default=False, verbose_name='Признак активации')
    mytoken = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

