from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Group №{self.pk} - {self.group_name}"
