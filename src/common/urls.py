from django.urls import path
from .views import RandomTimeView

urlpatterns = [
    path('random-time/', RandomTimeView.as_view(), name='random_time'),
]
