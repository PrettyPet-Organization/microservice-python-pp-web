from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models.custom_user import CustomUser
from accounts.validators import validate_age, validate_image
from profiles.models.cities import City


class Profile(models.Model):
    user = models.OneToOneField(
        to=CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True)
    public_name = models.CharField(_("Name"), blank=True, null=True, max_length=100)
    age = models.PositiveSmallIntegerField(
        _("Age"), blank=True, null=True, default=0, validators=[validate_age]
    )
    photo_url = models.ImageField(
        _("Photo url"), blank=True, null=True, validators=[validate_image]
    )
    description = models.TextField(_("Description"), blank=True, null=True)
    hobbies = models.CharField(_("Hobbies"), max_length=100, blank=True, null=True)
