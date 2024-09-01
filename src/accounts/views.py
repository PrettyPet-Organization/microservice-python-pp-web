from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect, render
from django.views import View

from accounts.models.profile import Profile
from settings.auth import FAILED_LOGIN_ATTEMPT_ID

from .forms import UserLoginForm, UserRegisterForm


def say_hi(request):
    return HttpResponse("<h1>Первые строчки проекта созданы</h1>")


# Регистрация поользователя
class UserRegisterView(View):
    template_name = "register.html"

    def get(self, request):
        form = UserRegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect("login")
        else:
            return render(request, self.template_name, {"form": form})


class UserLoginView(View):
    template_name = "login.html"

    def get(self, request):
        form = UserLoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if FAILED_LOGIN_ATTEMPT_ID not in request.session:
            request.session[FAILED_LOGIN_ATTEMPT_ID] = 0

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                request.session[FAILED_LOGIN_ATTEMPT_ID] = 0
                return redirect("say_hi")
            else:
                request.session[FAILED_LOGIN_ATTEMPT_ID] += 1
                form.add_error(None, "Некорректные данные")
                if request.session[FAILED_LOGIN_ATTEMPT_ID] >= 3:
                    form.add_error(None, "Попробуйте зайти с помощью кода из почты")
        else:
            request.session[FAILED_LOGIN_ATTEMPT_ID] += 1

        return render(request, self.template_name, {"form": form})


# Аутентификация по коду из почте (пока не работает!)
"""
class VerificationView(View):
    def post(self, request):
        form = CodeVerificationForm(request.POST)
        if form.is_valid():
            verification_word = form.cleaned_data.get('verification_word')

            if verification_word == request.session.get('verification_code'):
                # После успешной проверки кода, пользователю предоставляется доступ
                request.session['failed_login_attempts'] = 0
                user = CustomUsers.objects.get(username=request.session.get('username'))
                login(request, user)
                return redirect('say_hi')
            else:
                form.add_error(None, 'Неверный код.')
        return render(request, 'verification.html', {'form': form})
"""


class ProfileView(View, LoginRequiredMixin):
    def get(self):
        pass
