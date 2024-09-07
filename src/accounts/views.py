import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from accounts.forms import UserLoginForm, UserRegisterForm
from common.utils import create_and_send_email
from profiles.models.profiles import Profile
from settings import FAILED_LOGIN_ATTEMPTS_LIMIT

# Creating a logger
logger = logging.getLogger(__name__)


def say_hi(request):
    logger.info("Visited say_hi view")
    return HttpResponse("<h1>Первые строчки проекта созданы</h1>")


# User registration
class UserRegisterView(View):
    template_name = "register.html"

    def get(self, request):
        form = UserRegisterForm()
        logger.info("Rendering UserRegisterForm on GET request")
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            logger.info(f"User registered successfully: {user.username}")
            create_and_send_email(
                send_to=profile.user.email,
                template_name="emails/registration_success.html",
                context={"name": profile.user.username},
                subject="Успешная регистрация",
            )
            logger.info(f"User registered successfully: {user.username}")
            return redirect("login")
        else:
            logger.warning("User registration failed with errors")
            return render(request, self.template_name, {"form": form})


class UserLoginView(View):
    template_name = "login.html"
    failed_login_attempt_key = "failed_login_attempt_count"

    def get(self, request):
        form = UserLoginForm()
        logger.info("Rendering UserLoginForm on GET request")
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        request.session.setdefault(self.failed_login_attempt_key, 0)

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                request.session[self.failed_login_attempt_key] = 0
                logger.info(f"User logged in successfully: {email}")
                return redirect("say_hi")
            else:
                request.session[self.failed_login_attempt_key] += 1
                error_msg = _("Incorrect password or email")
                form.add_error(None, error_msg)
                logger.warning(f"Failed login attempt for email: {email}")
        else:
            request.session[self.failed_login_attempt_key] += 1
            logger.warning("Form validation failed during login attempt")

        if (
            request.session[self.failed_login_attempt_key]
            >= FAILED_LOGIN_ATTEMPTS_LIMIT
        ):
            form.add_error(None, _("Try logging using email"))
            logger.error(f"Login attempts exceeded limit for email: {email}")

        return render(request, self.template_name, {"form": form})


# Аутентификация по коду из почты (пока не работает!)
"""
class VerificationView(View):
    def post(self, request):
        form = CodeVerificationForm(request.POST)
        if form.is_valid():
            verification_word = form.cleaned_data.get('verification_word')

            if verification_word == request.session.get('verification_code'):
                request.session['failed_login_attempts'] = 0
                user = CustomUser.objects.get(username=request.session.get('username'))
                login(request, user)
                logger.info(f"User verified and logged in: {user.username}")
                return redirect('say_hi')
            else:
                form.add_error(None, 'Неверный код.')
                logger.warning("Invalid verification code entered")
        return render(request, 'verification.html', {'form': form})
"""


class ProfileView(View, LoginRequiredMixin):
    def get(self, request):
        logger.info("Rendering ProfileView")
        pass
