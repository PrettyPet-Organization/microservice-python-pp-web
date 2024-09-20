from rest_framework.serializers import ModelSerializer

from hackathons.models.participants_in_hackathon import ParticipantsInHackathon
from hackathons.serializers.groups_for_hackathons import GroupsForHackathonSerializer
from hackathons.serializers.roles_in_hackathon import RolesInHackathonSerializer
from hackathons.serializers.tools_in_hackathon import ToolsInHackathonSerializer


class ParticipantsInHackathonSerializer(ModelSerializer):
    roles = RolesInHackathonSerializer(many=True, source="rolesinhackathon_set")
    tools = ToolsInHackathonSerializer(many=True, source="toolsinhackathon_set")
    groups = GroupsForHackathonSerializer(many=True)

    class Meta:
        model = ParticipantsInHackathon
        fields = "__all__"
