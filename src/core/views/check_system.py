from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView


class CheckSystem(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        return JsonResponse(data)


class CheckLogs(APIView):
    def get(self, request):
        from settings.logging import example_logs, LOGGING

        data = {'message': 'Check logs'}

        example_logs(LOGGING)
        return JsonResponse(data)
