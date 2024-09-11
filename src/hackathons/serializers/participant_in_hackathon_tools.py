from rest_framework.serializers import ModelSerializer
from hackathons.models.participant_in_hackathon_tools import ParticipantInHackathonTools


class ParticipantInHackathonToolsSerializer(ModelSerializer):
    class Meta:
        model = ParticipantInHackathonTools
        fields = [
            "__all__"
        ]


