from django.db import models
from django.utils.translation import gettext_lazy as _
from hackathons.models.hackathons import Hackathons
from profiles.models.profiles import Profile


class ParticipantsInHackathon(models.Model):
    participant_id = models.IntegerField(verbose_name=_("participant id"))
    hackathon_id = models.ForeignKey(to=Hackathons, verbose_name=_("hackathon id"), on_delete=models.CASCADE)
    profile_id = models.ForeignKey(to=Profile, verbose_name=_("profile id"), on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.participant_id} | {self.hackathon_id} | {self.profile_id}'