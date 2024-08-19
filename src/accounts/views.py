from django.shortcuts import HttpResponse


def say_hi(request):
    return HttpResponse('<h1>Первые строчки проекта созданы</h1>')