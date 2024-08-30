from django.urls import path

from . import views

urlpatterns = [
    path('hi/', views.say_hi, name='say_hi'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    # path('verify/', views.VerificationView.as_view(), name='verify'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
