from django.http import JsonResponse
from rest_framework.views import APIView


class CheckLog(APIView):
    def get(self, request):
        data = {'message': 'Hello, World!'}
        return JsonResponse(data)
