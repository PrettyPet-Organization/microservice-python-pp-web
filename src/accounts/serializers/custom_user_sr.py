from rest_framework.serializers import ModelSerializer

from accounts.models.custom_user import CustomUser
from profiles.serializers.profile_sr import ProfileSerializer


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["username", "email", "profile"]
