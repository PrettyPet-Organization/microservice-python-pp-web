from django.shortcuts import render, HttpResponse


def say_hi(request):
    return HttpResponse('<h1>Первые строчки проекта созданы</h1>')