from rest_framework.serializers import ModelSerializer

from hackathons.models.tags_in_hackathon import TagsInHackathon


class RolesInHackathonSerializer(ModelSerializer):
    class Meta:
        model = TagsInHackathon
        fields = [
            "__all__"
        ]