from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons
from projects.models.tags_in_project import Tag


class TagsInHackathon(models.Model):
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_('hackathon id'), on_delete=models.CASCADE)
    tag_id = models.ForeignKey(to=Tag, verbose_name=_('tag id'), on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.hackathon_id} | {self.tag_id}'
