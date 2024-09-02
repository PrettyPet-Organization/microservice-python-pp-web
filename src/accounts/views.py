from django.shortcuts import HttpResponse, redirect, render
from .forms import UserRegisterForm, UserLoginForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models.profile import Profile
from settings.sessions import FAILED_LOGIN_ATTEMPTS_LIMIT
from django.contrib.auth import authenticate, login


def say_hi(request):
    return HttpResponse('<h1>Первые строчки проекта созданы</h1>')


class UserRegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        form = UserRegisterForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('login')
        else:
            return render(request, self.template_name, {"form": form})


class UserLoginView(View):
    template_name = 'login.html'
    failed_login_attempt_key = 'failed_login_attempt_count'

    def get(self, request):
        form = UserLoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = UserLoginForm(request.POST)

        request.session.setdefault(self.failed_login_attempt_key, 0)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                request.session[self.failed_login_attempt_key] = 0
                return redirect('say_hi')
            else:
                request.session[self.failed_login_attempt_key] += 1
                error_msg = 'Неправильно указали пароль или почту'
                form.add_error(None, error=error_msg)
        else:
            request.session[self.failed_login_attempt_key] += 1

        if request.session[self.failed_login_attempt_key] >= FAILED_LOGIN_ATTEMPTS_LIMIT:
            error_msg = 'Попробуйте зайти с помощью почты'
            form.add_error(None, error=error_msg)

        return render(request, self.template_name, {'form': form})


# Аутентификация по коду из почты (пока не работает!)
'''
class VerificationView(View):
    def post(self, request):
        form = CodeVerificationForm(request.POST)
        if form.is_valid():
            verification_word = form.cleaned_data.get('verification_word')

            if verification_word == request.session.get('verification_code'):
                # После успешной проверки кода, пользователю предоставляется доступ
                request.session['failed_login_attempts'] = 0
                user = CustomUser.objects.get(username=request.session.get('username'))
                login(request, user)
                return redirect('say_hi')
            else:
                form.add_error(None, 'Неверный код.')
        return render(request, 'verification.html', {'form': form})
'''


class ProfileView(View, LoginRequiredMixin):
    def get(self):
        pass
