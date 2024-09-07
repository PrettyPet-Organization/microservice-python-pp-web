from django.db import models


class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        NOT_STARTED = "not_started", "Not Started"
        IN_PROCESS = "in_process", "In Process"
        NOT_FINISHED = "not_finished", "Not Finished"
        FINISHED = "finished", "Finished"

    project_type = models.ForeignKey(
        to="ProjectType", on_delete=models.SET_NULL, null=True, related_name="projects"
    )
    project_name = models.CharField(max_length=100)
    core_idea = models.CharField(max_length=255)
    description = models.TextField()
    finish_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=12, choices=ProjectStatus.choices, default=ProjectStatus.NOT_STARTED
    )
    tools = models.ManyToManyField(
        to="Tool", through="ToolsInProject", related_name="projects"
    )
    roles = models.ManyToManyField(
        to="Role", through="RolesInProject", related_name="projects"
    )
    tags = models.ManyToManyField(to="Tag", related_name="projects")
    groups = models.ManyToManyField(to="Group", related_name="projects")
