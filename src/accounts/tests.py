from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.utils.translation import gettext as _


from accounts.models.custom_user import CustomUser
from accounts import messages


class UserRegistrationTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('register')
        self.valid_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
            'code_word': 'secret'
        }
        self.invalid_data_password_mismatch = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'DifferentPassword',
            'code_word': 'secret'
        }
        self.invalid_data_not_unique_email = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
        }
        # Create user for testing not unique email
        CustomUser.objects.create_user(
            username='existinguser',
            email='existinguser@example.com',
            password='Testpassword123'
        )

    def test_user_registration(self):
        """Test success registration user"""
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(CustomUser.objects.filter(email=self.valid_data['email']).exists())

    def test_registration_with_mismatched_passwords(self):
        """Test registration with mismatched passwords"""
        response = self.client.post(self.url, self.invalid_data_password_mismatch, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(_(messages.PASSWORDS_DONT_MATCH_ERROR_MESSAGE), response.data['non_field_errors'][0])

    def test_registration_with_not_unique_email(self):
        """Test registration with not unique email"""
        response = self.client.post(self.url, {
            'username': 'newuser',
            'email': 'existinguser@example.com',
            'password1': 'Testpassword123',
            'password2': 'Testpassword123',
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(_(messages.NOT_UNIQUE_EMAIL_ERROR_MESSAGE), response.data['email'])

    def test_registration_with_code_word(self):
        """Test registration with code word"""
        response = self.client.post(self.url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(email=self.valid_data['email'])
        self.assertEqual(user.code_word, self.valid_data['code_word'])

    def test_registration_without_code_word(self):
        """Test registration without code word"""
        data_without_code_word = self.valid_data.copy()
        data_without_code_word.pop('code_word')
        response = self.client.post(self.url, data_without_code_word, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(email=self.valid_data['email'])
        self.assertEqual(user.code_word, "")


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