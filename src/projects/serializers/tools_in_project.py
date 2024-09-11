from rest_framework.serializers import ModelSerializer

from projects.models.tools_in_project import Tool, ToolsInProject


class ToolsSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = [
            "tool_name",
        ]


class ToolsInProjectSerializer(ModelSerializer):
    class Meta:
        model = ToolsInProject
        fields = [
            "tool",
            "project",
            "participants_needed",
        ]
