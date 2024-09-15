from rest_framework.serializers import ModelSerializer

from projects.models.groups_for_projects import Group


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"
