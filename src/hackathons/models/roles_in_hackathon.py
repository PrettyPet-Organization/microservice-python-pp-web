from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons
from common.models.roles import Roles


class RolesInHackathon(models.Model):
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_('hackathon id'), on_delete=models.CASCADE)
    role_id = models.ForeignKey(to=Roles, verbose_name=_('role id'), on_delete=models.CASCADE)
    participants_needed = models.IntegerField(verbose_name=_('participants needed'), default=None)

    def __str__(self):
        return f'{self.hackathon_id} | {self.role_id}'