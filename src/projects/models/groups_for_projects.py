from django.db import models
from django.utils.translation import gettext_lazy as _


class Group(models.Model):
    group_name = models.CharField(verbose_name=_("Group name"), max_length=100)

    def __str__(self):
        return f"Group №{self.pk} - {self.group_name}"
