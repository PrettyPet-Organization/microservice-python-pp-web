from rest_framework.serializers import ModelSerializer

from hackathons.models.hackathons import Hackathon


class HackathonsSerializer(ModelSerializer):

    class Meta:
        model = Hackathon
        fields = "__all__"
