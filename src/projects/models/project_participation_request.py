from django.db import models

from profiles.models.profiles import Profile


class ProjectParticipationRequest(models.Model):
    class RequestStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"
        DECLINED = "declined", "Declined"

    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    project = models.ForeignKey(to="Project", on_delete=models.CASCADE)
    cover_letter = models.TextField()
    resume_url = models.URLField(blank=True, null=True)
    status = models.CharField(
        max_length=12, choices=RequestStatus.choices, default=RequestStatus.PENDING
    )

    def __str__(self):
        return f"Request №{self.pk} from {self.profile.user.username} for project №{self.project.pk} - {self.project}"
