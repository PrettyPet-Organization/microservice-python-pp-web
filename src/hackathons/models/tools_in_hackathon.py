from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons
from projects.models.tools_in_project import Tool


class ToolsInHackathon(models.Model):
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_('hackathon id'), on_delete=models.CASCADE)
    tool_id = models.ForeignKey(to=Tool, verbose_name=_('tool id'), on_delete=models.SET_NULL)
    participants_needed = models.IntegerField(verbose_name=_('participants needed'),
                                              default=None, blank=True, null=True)

    def __str__(self):
        return f'{self.hackathon_id} | {self.tool_id}'
