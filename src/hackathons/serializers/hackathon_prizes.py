from rest_framework.serializers import ModelSerializer
from hackathons.models.hackathon_prizes import HackathonPrizes


class HackathonPrizesSerializer(ModelSerializer):

    class Meta:
        model = HackathonPrizes
        fields = [
            "__all__"
        ]


