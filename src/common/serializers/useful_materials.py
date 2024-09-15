from rest_framework.serializers import ModelSerializer

from common.models.useful_materials import UsefulMaterial


class RolesInProjectSerializer(ModelSerializer):
    class Meta:
        model = UsefulMaterial
        fields = "__all__"
