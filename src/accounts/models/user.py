from hashlib import sha256
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.managers import CustomUserManager
from accounts.validators import validate_password, validate_phone_number


class CustomUser(AbstractUser):
    email = models.EmailField(_('Электронный адрес'), unique=True, max_length=255)
    phone_number = models.CharField(_('Номер телефона'), unique=True, blank=True, null=True, default=None,
                                    max_length=20, validators=[validate_phone_number])
    password = models.CharField(_('Пароль пользователя'), validators=[validate_password], max_length=255)
    code_word = models.CharField(_('Кодовое слово для входа'), max_length=12, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Установка кодового слово
    def set_code_word(self, code_word):
        self.code_word = sha256(code_word.encode()).hexdigest()

    # Проверка на совпадение кодового слово
    def check_code_word(self, code_word):
        return self.code_word == sha256(code_word.encode()).hexdigest()

    def __str__(self):
        return self.username
