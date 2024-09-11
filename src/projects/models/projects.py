from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        NOT_STARTED = "NS", _("Not Started")
        IN_PROCESS = "IP", _("In Process")
        NOT_FINISHED = "NF", _("Not Finished")
        FINISHED = "FN", _("Finished")

    project_type = models.ForeignKey(
        _("Type for project"), to="ProjectType", on_delete=models.SET_NULL, null=True, related_name="projects",
    )
    project_name = models.CharField(_("Project name"), max_length=100)
    core_idea = models.CharField(_("Core idea"), max_length=255)
    description = models.TextField(_("Description"))
    finish_date = models.DateField(_("End time for project"), null=True, blank=True)
    status = models.CharField(
        _("Actual status"), max_length=2, choices=ProjectStatus.choices, default=ProjectStatus.NOT_STARTED
    )
    tools = models.ManyToManyField(
        _("Tools for project"), to="Tool", through="ToolsInProject", related_name="projects"
    )
    roles = models.ManyToManyField(
        _("Role for project"), to="Role", through="RolesInProject", related_name="projects"
    )
    tags = models.ManyToManyField(_("Tags for project"), to="Tag", related_name="projects")
    groups = models.ManyToManyField(_("Groups for project"), to="Group", related_name="projects")

    @property
    def is_finished(self):
        return self.status == self.ProjectStatus.FINISHED

    def __str__(self):
        return f"Project №{self.pk} - {self.project_name}"
