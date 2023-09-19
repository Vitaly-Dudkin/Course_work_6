from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone_number', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='image', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Country', null=True, blank=True)
    comments = models.CharField(max_length=200, verbose_name='Country', null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
