from django.db import models

from profiles.models.profiles import Profile


class ParticipantInProject(models.Model):
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    roles = models.ManyToManyField(to="Role", through="RolesInProject")
    tools = models.ManyToManyField(to="Tool", through="ToolsInProject")
    groups = models.ManyToManyField(to="Group")

    def __str__(self):
        return f"Participant №{self.pk} in Project {self.project.pk} {self.project}"
