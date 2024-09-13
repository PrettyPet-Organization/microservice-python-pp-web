from django.db import models


class SocialLink(models.Model):
    link_name = models.CharField(max_length=100)
    url = models.URLField(max_length=255)
