from rest_framework.serializers import ModelSerializer

from hackathons.models.tools_in_hackathon import ToolsInHackathon


class RolesInHackathonSerializer(ModelSerializer):
    class Meta:
        model = ToolsInHackathon
        fields = [
            "__all__"
        ]
