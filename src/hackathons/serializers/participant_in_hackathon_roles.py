from rest_framework.serializers import ModelSerializer
from hackathons.models.participant_in_hackathon_roles import ParticipantInHackathonRoles
from roles_in_hackathon import RolesInHackathonSerializer


class ParticipantInHackathonRolesSerializer(ModelSerializer):
    roles = RolesInHackathonSerializer(many=True, source='rolesinhackathon_set')

    class Meta:
        model = ParticipantInHackathonRoles
        fields = [
            "__all__"
        ]


