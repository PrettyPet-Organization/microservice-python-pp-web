from rest_framework.serializers import ModelSerializer

from projects.models.project_types import ProjectType


class RolesSerializer(ModelSerializer):
    class Meta:
        model = ProjectType
        fields = "__all__"
