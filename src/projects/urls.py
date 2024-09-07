from projects import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'all', views.ProjectViewSet)
urlpatterns = router.urls
