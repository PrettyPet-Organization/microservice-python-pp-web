from django.db import models


class ProjectType(models.Model):
    type_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Type №{self.pk} - {self.type_name}"
