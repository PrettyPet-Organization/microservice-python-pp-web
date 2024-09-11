from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons


class GroupsInHackathon(models.Model):
    group_id = models.IntegerField(verbose_name=_("group id"))
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_("hackathon id"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.group_id} | {self.hackathon_id}'


