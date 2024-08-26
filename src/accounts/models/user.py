from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import CustomUserManager
from accounts.validators import validate_password, validate_phone_number


class CustomUser(AbstractUser):
    email = models.EmailField(_('Электронный адрес'), unique=True, max_length=255)
    phone_number = models.CharField(_('Номер телефона'), unique=True, blank=True, max_length=20,
                                    validators=[validate_phone_number])
    password = models.CharField(_('Пароль пользователя'), validators=[validate_password], max_length=255)
    code_word = models.CharField(_('Кодовое слово для входа'), max_length=12, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
