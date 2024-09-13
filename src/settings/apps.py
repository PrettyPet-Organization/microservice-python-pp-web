# Settings for registering Django applications and their configurations.

INSTALLED_APPS = [
    "accounts.apps.AuthConfig",
    "core.apps.CoreConfig",
    "profiles.apps.ProfilesConfig",
    "projects.apps.ProjectsConfig",
    "hackathons.apps.HackathonsConfig",
    "common.apps.CommonConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "rest_framework_simplejwt.token_blacklist",
]
