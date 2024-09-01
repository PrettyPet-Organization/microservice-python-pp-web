from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HackathonsConfig(AppConfig):
    name = "hackathons"
    verbose_name = _("Everything related to hackathons")
