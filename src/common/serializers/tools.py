from rest_framework.serializers import ModelSerializer

from common.models.tools import Tool


class ToolSerializer(ModelSerializer):
    class Meta:
        model = Tool
        fields = "__all__"
