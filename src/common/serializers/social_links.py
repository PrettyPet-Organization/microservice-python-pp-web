from rest_framework.serializers import ModelSerializer

from common.models.social_links import SocialLink


class SocialLinkSerializer(ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"
