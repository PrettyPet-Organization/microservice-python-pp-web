from rest_framework.serializers import ModelSerializer
from hackathons.models.participant_in_hackathon_groups import ParticipantInHackathonGroups


class ParticipantInHackathonGroupsSerializer(ModelSerializer):

    class Meta:
        model = ParticipantInHackathonGroups
        fields = [
            "__all__"
        ]


