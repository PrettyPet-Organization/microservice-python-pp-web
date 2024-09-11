from rest_framework.viewsets import GenericViewSet, mixins

from projects.models.projects import Project
from projects.serializers.projects import ProjectsSerializer


class ProjectViewSet(GenericViewSet, mixins.ListModelMixin):
    """
    A viewset for listing project instances.

    Provides the following action:
    - `list`: Retrieve a list of all projects.

    Attributes:
    - `queryset`: A queryset for retrieving project instances.
    - `serializer_class`: The serializer class used for validating and serializing data.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectsSerializer
