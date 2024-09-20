from django.db import models
from django.utils.translation import gettext_lazy as _

from hackathons.models.groups_for_hackathons import GroupsForHackathon
from hackathons.models.participants_in_hackathon import ParticipantsInHackathon


class ParticipantInHackathonGroups(models.Model):
    participant = models.ForeignKey(
        to=ParticipantsInHackathon,
        on_delete=models.CASCADE,
        verbose_name=_("participant"),
    )
    group = models.ForeignKey(
        to=GroupsForHackathon,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("group"),
    )

    def __str__(self):
        return f"{self.participant} | {self.group}"
