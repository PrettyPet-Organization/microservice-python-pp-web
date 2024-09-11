from django.db import models


class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Role №{self.pk} - {self.role_name}"


class RolesInProject(models.Model):
    role = models.ForeignKey(to="Role", on_delete=models.SET_NULL, null=True)
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)
    participants_needed = models.PositiveIntegerField(null=True, blank=True)
