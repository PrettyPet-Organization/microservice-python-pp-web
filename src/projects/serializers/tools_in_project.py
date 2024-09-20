from rest_framework.serializers import ModelSerializer

from common.serializers.tools import ToolSerializer
from projects.models.tools_in_project import ToolsInProject


class ToolsInProjectSerializer(ModelSerializer):
    tool = ToolSerializer()

    class Meta:
        model = ToolsInProject
        fields = "__all__"
