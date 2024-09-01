# Settings for the logging system, including log levels, formatting and handlers

import logging
import os
from pathlib import Path

from .common import BASE_DIR

LOGS_DIR = BASE_DIR.parent / "logs"

# Create a directory if it doesn't exist
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

LOGS_FILE_NAME = "logs"


class DebugAndInfoOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.DEBUG, logging.INFO)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "debug_and_info_only_filter": {
            "()": DebugAndInfoOnlyFilter,
        },
    },
    "formatters": {
        "custom_formatter": {
            "format": "{levelname} - {asctime} - {pathname}:{lineno} - {funcName}() - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "filters": ["debug_and_info_only_filter"],
            "formatter": "custom_formatter",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "custom_formatter",
            "filename": os.path.join(LOGS_DIR, LOGS_FILE_NAME),
            "when": "midnight",
            "backupCount": 3,
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "DEBUG",
    },
}
