from django.urls import path
from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register(r"all", views.ProjectViewSet)

urlpatterns = [path("frontprojects/",views.FrontPageProjectView.as_view(),name="frontpage_projects",)]

urlpatterns += router.urls
