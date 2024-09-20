from rest_framework.serializers import ModelSerializer

from common.models.roles import Role
from hackathons.models.roles_in_hackathon import RolesInHackathon


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RolesInHackathonSerializer(ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = RolesInHackathon
        fields = "__all__"
