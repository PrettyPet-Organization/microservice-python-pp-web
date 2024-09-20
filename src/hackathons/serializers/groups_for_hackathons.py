from rest_framework.serializers import ModelSerializer

from hackathons.models.groups_for_hackathons import GroupsForHackathon


class GroupsForHackathonSerializer(ModelSerializer):
    class Meta:
        model = GroupsForHackathon
        fields = "__all__"
