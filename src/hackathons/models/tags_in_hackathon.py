from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons


class TagsInHackathon(models.Model):
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_('hackathon id'), on_delete=models.CASCADE)
    tag_id = models.IntegerField(verbose_name=_('tag id'))

    def __str__(self):
        return f'{self.hackathon_id} | {self.tag_id}'
