from django.db import models


class ParticipantType(models.TextChoices):
    CREATOR = 'creator', 'Creator'
    ADMIN = 'admin', 'Admin'
    PARTICIPANT = 'participant', 'Participant'
