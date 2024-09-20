from rest_framework.serializers import ModelSerializer

from common.models.roles import Role


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
