from django.apps import AppConfig
from django.conf import settings
from django.urls import reverse


class CoreConfig(AppConfig):
    name = 'core'
    verbose_name = 'Общие утилиты проекта'

    def ready(self):
        self._log_startup_message()

    @staticmethod
    def _log_startup_message() -> None:
        """
        Logs a message indicating the successful startup of the project.

        Configures the logger using the settings defined in `settings.LOGGING` and logs an informational message
        containing a URL where the system status can be checked. If an error occurs while forming the URL or during
        logging, it logs the error message.

        :rtype: None

        :raises Exception: Logs any exception that occurs during URL formation or logging.
        """

        import logging.config

        logging_conf = settings.LOGGING
        logging.config.dictConfig(logging_conf)
        logger = logging.getLogger(__name__)

        try:
            url_path = reverse('check_logs')
            # TODO: Replace 'http://localhost:8000'
            base_url = 'http://localhost:8000'
            full_url = f'{base_url}{url_path}'

            logger.info(f'Проект запущен успешно. Вы можете проверить работу системы по данной ссылке: {full_url}')

        except Exception as e:
            logger.error(f'Ошибка при формировании сообщения о запуске: {e}')
