from rest_framework.serializers import ModelSerializer

from common.models.roles import Role
from projects.models.roles_in_project import RolesInProject


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class RolesInProjectSerializer(ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = RolesInProject
        fields = "__all__"
