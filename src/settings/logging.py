# Settings for the logging system, including log levels, formatting and handlers

import os
from pathlib import Path

from .common import BASE_DIR


LOGS_DIR = BASE_DIR.parent / 'logs'

# Create a directory if it doesn't exist
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

LOGS_FILE_NAME = 'logs'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'custom': {
            'format': '{levelname} - {asctime} - {pathname}:{lineno} - {funcName}() - {message}',
            'style': '{',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'custom',
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'formatter': 'custom',
            'filename': os.path.join(LOGS_DIR, LOGS_FILE_NAME),
            'when': 'midnight',
            'backupCount': 3,
        },
    },

    'root': {
        'handlers': ['console', 'file'],
        'level': 'DEBUG',
    },
}


def example_logs(logging_conf: dict) -> None:
    """
    Processes examples of logs of different levels.

    Initializes the logger based on the provided configuration and processes logs of various levels: DEBUG, INFO,
    WARNING, ERROR, and CRITICAL.

    :param logging_conf: Logging configuration as a dictionary.
    :type logging_conf: dict

    :rtype: None

    :raises ImportError: If the logging.config module could not be imported.
    :raises KeyError: If a required key is missing from the logging configuration.
    :raises Exception: To handle any other exceptions that may occur during setting up or using logging.
    """

    try:
        import logging.config

        logging.config.dictConfig(logging_conf)

        logger = logging.getLogger(__name__)

        logger.debug('example DEBUG message')
        logger.info('example INFO message')
        logger.warning('example WARNING message')
        logger.error('example ERROR message')
        logger.critical('example CRITICAL message')

    except ImportError as e:
        print(f'Module import exception: {e}')
    except KeyError as e:
        print(f'Logging configuration error: missing key {e}')
    except Exception as e:
        print(f'An error occurred while setting up logging: {e}')
