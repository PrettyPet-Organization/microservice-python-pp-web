from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"user_list", views.UserViewSet)

urlpatterns = [
    path("hi/", views.say_hi, name="say_hi"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("", include(router.urls)),
    # path('verify/', views.VerificationView.as_view(), name='verify'),
]
