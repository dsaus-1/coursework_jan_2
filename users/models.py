from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}

class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='почта', unique=True)
    phone = models.CharField(max_length=25, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='страна', **NULLABLE)
    token = models.CharField(max_length=15, verbose_name='токен')
    token_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания токена')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
