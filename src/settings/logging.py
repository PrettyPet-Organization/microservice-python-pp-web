# Settings for the logging system, including log levels, formatting and handlers

import os
from pathlib import Path

from .common import BASE_DIR

LOGS_DIR = BASE_DIR.parent / "logs"

# Create a directory if it doesn't exist
Path(LOGS_DIR).mkdir(parents=True, exist_ok=True)

LOGS_FILE_NAME = "logs"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom": {
            "format": "{levelname} - {asctime} - {pathname}:{lineno} - {funcName}() - {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "custom",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "custom",
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
