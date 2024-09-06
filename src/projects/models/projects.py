from django.db import models

from .project_types import ProjectType
from .roles_in_project import ProjectToRole, Role
from .tools_in_project import Tool
from .tags_in_project import Tag


class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        NOT_STARTED = "not_started", "Not Started"
        IN_PROCESS = "in_process", "In Process"
        NOT_FINISHED = "not_finished", "Not Finished"
        FINISHED = "finished", "Finished"

    project_type = models.ForeignKey(
        to=ProjectType, on_delete=models.SET_NULL, null=True
    )
    project_name = models.CharField(max_length=100)
    core_idea = models.CharField(max_length=255)
    description = models.TextField()
    finish_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=2, choices=ProjectStatus.choices, default=ProjectStatus.NOT_STARTED
    )
    tools = models.ManyToManyField(to=Tool, related_name="projects")
    roles = models.ManyToManyField(
        to=Role, through=ProjectToRole, related_name="projects"
    )
    tags = models.ManyToManyField(to=Tag, related_name="projects")
