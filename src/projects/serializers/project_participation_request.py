from rest_framework.serializers import ModelSerializer

from projects.models.project_participation_request import ProjectParticipationRequest


class ParticipationRequestSerializer(ModelSerializer):
    class Meta:
        model = ProjectParticipationRequest
        fields = "__all__"
