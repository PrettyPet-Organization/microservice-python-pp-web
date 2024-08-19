"""
Конфигурации для подключения и настройки базы данных,
включая параметры подключения, использование пула соединений и настройки репликации.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
