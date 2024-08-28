# Конфигурации для подключения и настройки базы данных, включая параметры подключения, использование пула соединений и
# настройки репликации.

from .common import BASE_DIR


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
