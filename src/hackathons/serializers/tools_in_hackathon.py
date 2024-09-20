from rest_framework.serializers import ModelSerializer

from common.models.tools import Tool
from hackathons.models.tools_in_hackathon import ToolsInHackathon


class ToolSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"


class ToolsInHackathonSerializer(ModelSerializer):
    tool = ToolSerializer(many=True)

    class Meta:
        model = ToolsInHackathon
        fields = "__all__"
