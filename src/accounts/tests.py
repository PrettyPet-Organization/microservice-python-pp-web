from django.test import TestCase
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from accounts.models.custom_user import CustomUser


class UserRegistrationTest(TestCase):

    def test_user_registration(self):
        # Registration details
        registration_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "Strongpassword123",
            "password2": "Strongpassword123",
        }

        # Sending a POST request for registration
        response = self.client.post(reverse("register"), data=registration_data)

        # Verifying that registration was successful and the user was redirected to the login page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        # Verifying that the user has been created in the database
        user_exists = CustomUser.objects.filter(username="testuser").exists()
        self.assertTrue(user_exists)

    def test_registration_with_mismatched_passwords(self):
        # Data with mismatched passwords
        registration_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "Strongpassword123",
            "password2": "weakpassword321",
        }

        # Sending a POST request for registration
        response = self.client.post(reverse("register"), data=registration_data)

        # Checking that registration failed
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _("Passwords don't match"))

        # Checking that the user has not been created
        user_exists = CustomUser.objects.filter(username="testuser").exists()
        self.assertFalse(user_exists)


class UserLoginTest(TestCase):

    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="Strongpassword123",
        )

    def test_user_login_successful(self):
        # Login details
        login_data = {
            "email": "testuser@example.com",
            "password": "Strongpassword123",
        }

        # Sending a POST login request
        response = self.client.post(reverse("login"), data=login_data)

        # Checking that the login was successful and the user was redirected to the main page
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("say_hi"))

        # Verifying that the user is authenticated
        self.assertTrue(
            self.client.login(
                email="testuser@example.com", password="Strongpassword123"
            )
        )

    def test_login_with_wrong_password(self):
        # Data with incorrect password
        login_data = {
            "email": "testuser@example.com",
            "password": "wrongpassword",
        }

        # Sending a POST login request
        response = self.client.post(reverse("login"), data=login_data)

        # Checking if login failed
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, _("Incorrect password or email"))

        # Checking that the user is not authenticated
        self.assertFalse(
            self.client.login(email="testuser@example.com", password="wrongpassword")
        )
