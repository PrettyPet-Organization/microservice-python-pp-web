from django.db import models
from django.utils.translation import gettext_lazy as _


class City(models.Model):
    name = models.CharField(_('Город'), max_length=100)
    slug = models.SlugField(max_length=100, unique=True)