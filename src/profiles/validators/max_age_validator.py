from datetime import date

from dateutil.relativedelta import relativedelta
from django.core.validators import MaxValueValidator
from django.utils.translation import gettext_lazy as _


class MaxAgeValidator(MaxValueValidator):
    """
    A validator that ensures that the user's (Profile's) age is less than or equal to a specified age limit.
    """

    message = _("Age cannot be more than %(limit_value)s years.")
    code = "max_age"

    def __call__(self, value: date) -> None:
        super().__call__(value=relativedelta(date.today(), value).years)
