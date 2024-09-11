from rest_framework.serializers import ModelSerializer
from hackathons.models.hackathons import Hackathons


class HackathonsSerializer(ModelSerializer):

    class Meta:
        model = Hackathons
        fields = [
            "__all__"
        ]


