from rest_framework.serializers import ModelSerializer
from projects.models.projects import Project


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "project_type",
            "project_name",
            "core_idea",
            "description",
            "finish_date",
            "status",
            "tools",
            "roles",
            "tags",
            "groups",
        ]
