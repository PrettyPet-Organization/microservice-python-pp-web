from django.db import models
from django.utils.translation import gettext_lazy as _


class ProjectType(models.Model):
    type_name = models.CharField(_("Type name"), max_length=100)

    def __str__(self):
        return f"Type №{self.pk} - {self.type_name}"
