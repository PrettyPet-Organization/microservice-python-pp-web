from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Hackathons(models.Model):
    hackathon_id = models.AutoField(primary_key=True, verbose_name=_("hackathon id"))
    type_id = models.IntegerField(verbose_name=_("type id"), blank=True, null=True)
    name = models.CharField(verbose_name=_("name"), max_length=40, blank=True, null=True)
    core_idea = models.CharField(verbose_name=_("core idea"), max_length=40, blank=True, null=True)
    task = models.TextField(verbose_name=_("task"), max_length=400, blank=True, null=True)
    start_date = models.DateField(verbose_name=_("start date"), default=timezone.now)
    finish_date = models.DateField(verbose_name=_("finish date"), blank=True, null=True)
    image_url = models.CharField(verbose_name=_("image url"), blank=True, null=True)
    prize_id = models.IntegerField(verbose_name=_("prize id"), blank=True, null=True)

    def __str__(self):
        return f'{self.name} | №{self.hackathon_id}'


@receiver(pre_save, sender=Hackathons)
def set_start_date(sender, instance, *kwargs):
    if not instance.start_date:
        instance.start_date = timezone.now().date()
