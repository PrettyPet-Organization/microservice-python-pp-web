from django.urls import path
from .views.check_system import CheckLog

urlpatterns = [
    path('check-logs/', CheckLog.as_view(), name='check_logs'),
]