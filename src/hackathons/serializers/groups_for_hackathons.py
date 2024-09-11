from rest_framework.serializers import ModelSerializer

from hackathons.models.groups_for_hackathons import GroupsForHackathons


class GroupForHackathonsSerializer(ModelSerializer):
    class Meta:
        model = GroupsForHackathons
        fields = [
            "__all__",
        ]