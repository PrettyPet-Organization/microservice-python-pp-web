from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Tag №{self.pk} - {self.tag_name}"
