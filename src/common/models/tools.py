from django.db import models
from django.utils.translation import gettext_lazy as _


class Tool(models.Model):
    tool_name = models.CharField(_("Tool name"), max_length=100)

    def __str__(self):
        return f"Tool №{self.pk} - {self.tool_name}"
