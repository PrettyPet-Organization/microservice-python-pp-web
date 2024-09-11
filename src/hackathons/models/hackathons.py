from django.db import models
from django.utils.translation import gettext_lazy as _


class Hackathons(models.Model):
    hackathon_id = models.AutoField(verbose_name=_("hackathon id"))
    type_id = models.IntegerField(verbose_name=_("type id"))
    name = models.CharField(verbose_name=_("name"), max_length=40)
    core_idea = models.CharField(verbose_name=_("core idea"), max_length=40)
    task = models.TextField(verbose_name=_("task"), max_length=400)
    start_date = models.DateField(verbose_name=_("start date"))
    finish_date = models.DateField(verbose_name=_("finish date"))
    image_url = models.CharField(verbose_name=_("image url"))
    prize_id = models.IntegerField(verbose_name=_("prize id"))

    def __str__(self):
        return f'{self.hackathon_id} | {self.name}'
