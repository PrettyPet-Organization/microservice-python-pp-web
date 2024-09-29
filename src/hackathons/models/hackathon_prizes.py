from django.db import models
from django.utils.translation import gettext_lazy as _

from hackathons.models.hackathons import Hackathon


class HackathonPrizes(models.Model):
    prize = models.ManyToManyField(to=Hackathon, verbose_name=_("prize"))
    name = models.CharField(blank=True, null=True, max_length=40, verbose_name=_("name"))
    description = models.CharField(blank=True, null=True, max_length=200, verbose_name=_("description"))
    image_url = models.CharField(blank=True, null=True, max_length=100, verbose_name=_("image url"))

    def __str__(self):
        return f"{self.prize} | {self.name}"
