from django.db import models
from django.utils.translation import gettext_lazy as _

from profiles.models.profiles import Profile


class ParticipantInProject(models.Model):
    project = models.ForeignKey(
        _("Actual project"), to="Project", on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        _("Participant profile"), to=Profile, on_delete=models.CASCADE
    )
    roles = models.ManyToManyField(
        _("Participant roles"), to="Role", through="RolesInProject"
    )
    tools = models.ManyToManyField(
        _("Participant tools"), to="Tool", through="ToolsInProject"
    )
    groups = models.ManyToManyField(_("Participant groups"), to="Group")

    def __str__(self):
        return f"Participant №{self.pk} in Project {self.project.pk} {self.project}"
