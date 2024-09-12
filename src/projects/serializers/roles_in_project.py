from rest_framework.serializers import ModelSerializer

from projects.models.roles_in_project import Role, RolesInProject


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = [
            "role_name",
        ]


class RolesInProjectSerializer(ModelSerializer):
    role = RoleSerializer()

    class Meta:
        model = RolesInProject
        fields = [
            "role",
            "project",
            "participants_needed",
        ]
