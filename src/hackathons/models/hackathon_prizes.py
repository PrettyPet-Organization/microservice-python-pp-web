from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons


class HackathonPrizes(models.Model):
    prize_id = models.ManyToManyField(to=Hackathons, verbose_name=_("prize id"))
    name = models.CharField(verbose_name=_("name"))
    description = models.CharField(verbose_name=_("description"))
    image_url = models.CharField(verbose_name=_("image url"))

    def __str__(self):
        return f'{self.prize_id} | {self.name}'
