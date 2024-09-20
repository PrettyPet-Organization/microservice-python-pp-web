from rest_framework.serializers import ModelSerializer

from common.models.topics import Topic


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"
