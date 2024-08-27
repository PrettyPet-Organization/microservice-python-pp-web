import logging.config

from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView


def check_logs():
    logging_conf = settings.LOGGING
    logging.config.dictConfig(logging_conf)
    logger = logging.getLogger(__name__)

    try:
        logger.debug("example DEBUG message")
        logger.info("example INFO message")
        logger.warning("example WARNING message")
        logger.error("example ERROR message")
        logger.critical("example CRITICAL message")
        return True
    except ImportError as exc:
        print(f"Module import exception: {exc}")
        return None


class CheckSystem(APIView):
    def get(self, request):
        data = {}
        check_logs()
        data["logs"] = "Успешно настроились"
        if not check_logs():
            raise Exception("В проекте не настроено логирование.")

        return JsonResponse(data)
