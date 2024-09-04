from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AuthConfig(AppConfig):
    name = "accounts"
    verbose_name = _("Authorization/authentication")
