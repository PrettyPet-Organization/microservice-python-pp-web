from django.db import models


class ProjectType(models.Model):
    type_name = models.CharField(max_length=100)
