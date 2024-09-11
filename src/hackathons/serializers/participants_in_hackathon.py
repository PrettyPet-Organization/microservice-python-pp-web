from rest_framework.serializers import ModelSerializer
from hackathons.models.participants_in_hackathon import ParticipantsInHackathon


class ParticipantsInHackathonSerializer(ModelSerializer):
    class Meta:
        model = ParticipantsInHackathon
        fields = [
            "__all__"
        ]


