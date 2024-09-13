from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    tag_name = models.CharField(_("Tag name"), max_length=100)

    def __str__(self):
        return f"Tag №{self.pk} - {self.tag_name}"
