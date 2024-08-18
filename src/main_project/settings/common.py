from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-j*-^aoo$*1x7qe(xc-n-&%89o_)nn4)cp363rit_54hdz=i8*7'

DEBUG = True

ALLOWED_HOSTS = ['*']
ROOT_URLCONF = 'main.urls'

WSGI_APPLICATION = 'main.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'