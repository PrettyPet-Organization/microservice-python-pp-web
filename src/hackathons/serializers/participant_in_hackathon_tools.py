from rest_framework.serializers import ModelSerializer

from hackathons.models.participant_in_hackathon_tools import ParticipantInHackathonTools
from hackathons.serializers.tools_in_hackathon import ToolsInHackathonSerializer


class ParticipantInHackathonToolsSerializer(ModelSerializer):
    tools = ToolsInHackathonSerializer(many=True, source="toolsinhackathon_set")

    class Meta:
        model = ParticipantInHackathonTools
        fields = "__all__"
