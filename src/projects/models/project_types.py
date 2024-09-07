from django.db import models


class ProjectType(models.Model):
    tag_name = models.CharField(max_length=100)
