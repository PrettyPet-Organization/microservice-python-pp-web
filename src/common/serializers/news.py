from rest_framework.serializers import ModelSerializer

from common.models.news import News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
