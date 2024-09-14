from django.shortcuts import render
from rest_framework.request import Request

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _

from datetime import datetime
from random import choice
import pytz
import pycountry

class RandomTimeView(APIView):
    """
    A representation function that returns a random country
    and its time in the format '%H:%M:%S'
    results as a JSON response.

    :param request: The rest_framework Request object.
    :type request: Request

    :return: random country and time
    :rtype: Response
    """

    def get(self, request: Request) -> Response:
        random_country = choice(list(pycountry.countries))
        country_name = _(random_country.name)
        tz_name = pytz.timezone(pytz.country_timezones.get(random_country.alpha_2, [])[0])
        current_time = datetime.now(tz_name)

        return Response({'country': country_name, 'time': current_time.strftime("%H:%M:%S")})

