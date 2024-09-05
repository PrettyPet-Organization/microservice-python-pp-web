from rest_framework.serializers import ModelSerializer

from profiles.models.profiles import Profile


class ProfileSerializer(ModelSerializer):

    class Meta:
        model = Profile
        fields = ["user", "city", "public_name", "age", "description", "hobbies"]
