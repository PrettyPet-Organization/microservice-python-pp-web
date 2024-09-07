from rest_framework.viewsets import ModelViewSet
from projects.models.projects import Project
from projects.serializers.projects_sr import ProjectsSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
