from django.db import models
from django.utils.translation import gettext_lazy as _


class UsefulMaterial(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    description = models.CharField(max_length=1000, verbose_name=_("Description"))
    image_url = models.ImageField(verbose_name=_("Image"))
    link_name = models.CharField(max_length=100, verbose_name=_("Link name"))
    likes = models.PositiveIntegerField(default=0, verbose_name=_("Likes counter"))
