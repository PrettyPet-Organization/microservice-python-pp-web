from django.shortcuts import HttpResponse, redirect, render
from .forms import RegisterUserForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models.profile import Profile

def say_hi(request):
    return HttpResponse('<h1>Первые строчки проекта созданы</h1>')


# Регистрация поользователя
class RegisterView(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, "register.html", {"form": form})
    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect("login")
        else:
            return HttpResponse('error')

def login(request):
    pass


class ProfileView(View, LoginRequiredMixin):
    def get(self):
        pass
