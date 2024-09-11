from rest_framework.serializers import ModelSerializer

from hackathons.models.roles_in_hackathon import RolesInHackathon


class RolesInHackathonSerializer(ModelSerializer):
    class Meta:
        model = RolesInHackathon
        fields = [
            "__all__"
        ]
