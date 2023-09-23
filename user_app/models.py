from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone_number', null=True, blank=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='image', null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='Country', null=True, blank=True)
    verification_code = models.CharField(unique=True, null=True, blank=True, verbose_name='verification_code')
    is_active = models.BooleanField("active",
                                    default=False,
                                    help_text=(
                                        "Designates whether this user should be treated as active. "
                                        "Unselect this instead of deleting accounts."
                                    ),
                                    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
