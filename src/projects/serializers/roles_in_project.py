from rest_framework.serializers import ModelSerializer

from common.serializers.roles import RoleSerializer
from projects.models.roles_in_project import RolesInProject


class RolesInProjectSerializer(ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = RolesInProject
        fields = "__all__"
