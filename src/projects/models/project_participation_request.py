from django.db import models
from django.utils.translation import gettext_lazy as _

from profiles.models.profiles import Profile


class ProjectParticipationRequest(models.Model):
    class RequestStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        ACCEPTED = "accepted", "Accepted"
        DECLINED = "declined", "Declined"

    project = models.ForeignKey(
        _("Requested project"), to="Project", on_delete=models.CASCADE
    )
    profile = models.ForeignKey(
        _("Participant profile"), to=Profile, on_delete=models.CASCADE
    )
    cover_letter = models.TextField(_("Cover letter"))
    resume_url = models.URLField(_("Resume url"), blank=True, null=True)
    status = models.CharField(
        _("Status the request"),
        max_length=12,
        choices=RequestStatus.choices,
        default=RequestStatus.PENDING,
    )

    def __str__(self):
        return f"Request №{self.pk} from {self.profile.user.username} for project №{self.project.pk} - {self.project}"
