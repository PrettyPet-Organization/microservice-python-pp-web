import logging

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponse, redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts import messages
from accounts.serializers import UserRegisterSerializer
from profiles.models import Profile
from accounts.forms import UserLoginForm, UserRegisterForm
from settings import FAILED_LOGIN_ATTEMPTS_LIMIT

# Creating a logger
logger = logging.getLogger(__name__)


def say_hi(request):
    logger.info("Visited say_hi view")
    return HttpResponse("<h1>Первые строчки проекта созданы</h1>")



class UserRegisterView(APIView):
    """
    Handles user registration.

    Inherits from `APIView` and manages user creation by handling POST requests
    with user registration data. Upon successful registration, a 201 (Created)
    status is returned. If the request contains invalid data, a 400 (Bad Request)
    status is returned with validation errors.

    Methods:
        post(request):
            Handles user registration by validating the input data with
            `UserRegisterSerializer`. Returns HTTP 201 if successful or
            HTTP 400 in case of validation failure.
    """

    @extend_schema(
        description="Endpoint to register a new user. Accepts user registration data in the request body.",
        request=UserRegisterSerializer,
        responses={
            201: messages.USER_SUCCESSFULLY_REGISTERED_MESSAGE,
            400: messages.VALIDATION_ERROR_MESSAGE,
        },
    )
    def post(self, request):
        """
        Processes a POST request to register a new user.

        Args:
            request (Request): The HTTP request object containing user registration data.

        Returns:
            Response:
                - HTTP 201 (Created) if the user is successfully registered.
                - HTTP 400 (Bad Request) if the input data fails validation.
        """
        logger.info("Received registration request: %s", request.data)
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(messages.USER_SUCCESSFULLY_REGISTERED_MESSAGE)
            return Response(status=status.HTTP_201_CREATED)

        logger.warning("User registration failed: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
