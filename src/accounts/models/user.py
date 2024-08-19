from django.contrib.auth.models import AbstractUser
from django.db import models

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField("Электронный адрес", unique=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
