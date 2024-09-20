from rest_framework.serializers import ModelSerializer

from hackathons.models.groups_in_hackathon import GroupsInHackathon


class GroupInHackathonsSerializer(ModelSerializer):
    class Meta:
        model = GroupsInHackathon
        fields = "__all__"
