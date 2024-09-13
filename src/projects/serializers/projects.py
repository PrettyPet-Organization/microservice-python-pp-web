from rest_framework.serializers import ModelSerializer

from projects.models.projects import Project
from projects.serializers.groups_for_project import GroupSerializer
from projects.serializers.roles_in_project import RolesInProjectSerializer
from projects.serializers.tags_in_project import TagsSerializer
from projects.serializers.tools_in_project import ToolsInProjectSerializer


class ProjectsSerializer(ModelSerializer):
    roles = RolesInProjectSerializer(many=True, source="rolesinproject_set")
    tools = ToolsInProjectSerializer(many=True, source="toolsinproject_set")
    tags = TagsSerializer(many=True)
    groups = GroupSerializer(many=True)

    class Meta:
        model = Project
        fields = "__all__"
