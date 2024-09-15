from django.db import models
from django.utils.translation import gettext_lazy as _
from participants_in_hackathon import ParticipantsInHackathon
from projects.models.roles_in_project import Role


class ParticipantInHackathonRoles(models.Model):
    participant_id = models.ForeignKey(to=ParticipantsInHackathon,
                                       verbose_name=_("participant id"), on_delete=models.CASCADE)
    role_id = models.ForeignKey(to=Role,
                                verbose_name=_("role id"), on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.participant_id} | {self.role_id}'
