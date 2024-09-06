from django.db import models

from profiles.models.profiles import Profile
from projects.models.participant_types import ParticipantType
from projects.models.projects import Project
from projects.models.roles_in_project import Role


class ParticipantInfo(models.Model):

    participant_type = models.CharField(max_length=20, choices=ParticipantType.choices)
    role = models.ForeignKey(to=Role, on_delete=models.CASCADE)


class ProjectParticipants(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    participant_info = models.OneToOneField(
        to=ParticipantInfo, on_delete=models.CASCADE
    )
