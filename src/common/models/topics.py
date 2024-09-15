from django.db import models
from django.utils.translation import gettext_lazy as _


class Topic(models.Model):
    topic_name = models.CharField(max_length=100, verbose_name=_("Topic name"))
