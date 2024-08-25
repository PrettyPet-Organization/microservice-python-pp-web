from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models.user import CustomUser


class Profile(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE, verbose_name=_('Пользователь'), related_name='profile')
    city_name = models.CharField(_('Город'), blank=True, null=True, max_length=100)
    public_name = models.CharField(_('Имя'), blank=True, null=True, max_length=100)
    age = models.PositiveSmallIntegerField(_('Возраст'),blank=True, null=True, default=0)
    photo_url = models.ImageField(_('Путь к фото'), blank=True, null=True)
    description = models.TextField(_('Описание'))
    hobbies = models.CharField(_('Хобби'), max_length=100)

