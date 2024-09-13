from rest_framework.serializers import ModelSerializer

from common.models.tools import Tool
from projects.models.tools_in_project import ToolsInProject


class ToolsSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class ToolsInProjectSerializer(ModelSerializer):
    class Meta:
        model = ToolsInProject
        fields = "__all__"
