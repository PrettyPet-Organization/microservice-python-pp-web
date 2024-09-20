from rest_framework.serializers import ModelSerializer

from common.models.tags import Tag
from hackathons.models.tags_in_hackathon import TagsInHackathon


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class TagsInHackathonSerializer(ModelSerializer):
    tag = TagsSerializer(many=True)

    class Meta:
        model = TagsInHackathon
        fields = ["__all__"]
