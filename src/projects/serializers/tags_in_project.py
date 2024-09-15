from rest_framework.serializers import ModelSerializer

from common.models.tags import Tag


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
