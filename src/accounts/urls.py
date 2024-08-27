from django.urls import path

from . import views

urlpatterns = [
    path('hi/', views.say_hi, name='say_hi'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.say_hi, name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
