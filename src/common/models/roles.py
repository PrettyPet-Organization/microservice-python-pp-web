from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    role_name = models.CharField(_("Role name"), max_length=100)

    def __str__(self):
        return f"Role №{self.pk} - {self.role_name}"
