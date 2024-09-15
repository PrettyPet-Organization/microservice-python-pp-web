from django.db import models
from django.utils.translation import gettext_lazy as _
from participants_in_hackathon import ParticipantsInHackathon
from projects.models.tools_in_project import Tool


class ParticipantInHackathonTools(models.Model):
    participant_id = models.ForeignKey(to=ParticipantsInHackathon,
                                       verbose_name=_("participant id"), on_delete=models.CASCADE)
    tool_id = models.ForeignKey(to=Tool,
                                verbose_name=_("tool id"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.participant_id} | {self.tool_id}'

