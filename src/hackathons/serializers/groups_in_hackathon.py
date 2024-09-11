from rest_framework.serializers import ModelSerializer

from hackathons.models.groups_in_hackathon import GroupsInHackathon


class GroupsInHackathonsSerializer(ModelSerializer):
    class Meta:
        model = GroupsInHackathon
        fields = [
            "group_id",
            "hackathon_id"
        ]
