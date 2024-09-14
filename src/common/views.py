from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from pytz import timezone
from datetime import datetime
from random import choice

class RandomTimeView(APIView):
    '''A representation function that returns a random country
    and its time in the format '%H:%M:%S'

    Provides the following actions:
    by url 'common/random_time' returns the required data

    Attributes:
    - country_and_tz dictionary with the key country and the value time zone of the country
    - country random country
    - tz_name Press the time zone of this country
    -current_time current time in the selected country.
    To get this time the pytz and datetime library is used
    '''

    def get(self, request):
        country_and_tz =  {
            "Россия": "Europe/Moscow",
            "США": "America/New_York",
            "Канада": "America/Toronto",
            "Бразилия": "America/Sao_Paulo",
            "Австралия": "Australia/Sydney",
            "Китай": "Asia/Shanghai",
            "Индия": "Asia/Kolkata",
            "Япония": "Asia/Tokyo",
            "Германия": "Europe/Berlin",
            "Франция": "Europe/Paris",
            "Италия": "Europe/Rome",
            "Испания": "Europe/Madrid",
            "Великобритания": "Europe/London",
            "Мексика": "America/Mexico_City",
            "Южная Корея": "Asia/Seoul",
            "Новая Зеландия": "Pacific/Auckland",
            "Аргентина": "America/Argentina/Buenos_Aires",
            "Норвегия": "Europe/Oslo",
            "Швеция": "Europe/Stockholm",
            "Дания": "Europe/Copenhagen",
            "Польша": "Europe/Warsaw",
            "Турция": "Europe/Istanbul",
            "Нидерланды": "Europe/Amsterdam",
            "Индонезия": "Asia/Jakarta",
            "Филиппины": "Asia/Manila"
        }

        country = choice(list(country_and_tz))
        tz_name = timezone(country_and_tz[country])
        current_time = datetime.now(tz_name)

        return Response({'country': country, 'time': current_time.strftime("%H:%M:%S")})

