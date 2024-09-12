from rest_framework.serializers import ModelSerializer

from projects.models.participants_in_project import ParticipantInProject
from projects.serializers.groups_for_project import GroupSerializer
from projects.serializers.roles_in_project import RolesInProjectSerializer
from projects.serializers.tools_in_project import ToolsInProjectSerializer


class ParticipantSerializer(ModelSerializer):
    roles = RolesInProjectSerializer(many=True, source="rolesinproject_set")
    tools = ToolsInProjectSerializer(many=True, source="toolsinproject_set")
    groups = GroupSerializer(many=True)

    class Meta:
        model = ParticipantInProject
        fields = ["project", "profile", "roles", "tools", "groups"]
