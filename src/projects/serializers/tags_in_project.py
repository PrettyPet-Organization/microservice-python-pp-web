from rest_framework.serializers import ModelSerializer

from projects.models.tags_in_project import Tag


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            "tag_name",
        ]
