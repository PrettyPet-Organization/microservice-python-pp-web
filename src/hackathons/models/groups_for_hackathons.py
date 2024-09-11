from django.db import models
from django.utils.translation import gettext_lazy as _
from groups_in_hackathon import GroupsInHackathon


class GroupsForHackathons(models.Model):
    group_id = models.ForeignKey(to=GroupsInHackathon, verbose_name=_("group id"), on_delete=models.CASCADE)
    group_name = models.CharField(verbose_name=_("group name"))

    def __str__(self):
        return f'{self.group_id} | {self.group_name}'
