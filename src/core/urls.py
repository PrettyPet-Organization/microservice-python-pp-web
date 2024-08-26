from django.urls import path
from .views.check_system import CheckLogs


urlpatterns = [
    path('check-logs/', CheckLogs.as_view(), name='check_logs'),
]
