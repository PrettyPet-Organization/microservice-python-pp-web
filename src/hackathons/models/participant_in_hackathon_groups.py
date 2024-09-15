from django.db import models
from django.utils.translation import gettext_lazy as _
from participants_in_hackathon import ParticipantsInHackathon
from groups_for_hackathons import GroupsForHackathons


class ParticipantInHackathonGroups(models.Model):
    participant_id = models.ForeignKey(to=ParticipantsInHackathon,
                                       verbose_name=_("participant id"), on_delete=models.CASCADE)
    group_id = models.ForeignKey(to=GroupsForHackathons,
                                 verbose_name=_("group id"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.participant_id} | {self.group_id}'

