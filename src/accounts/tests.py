from django.test import TestCase
from django.urls import reverse
from accounts.models.user import CustomUser


class UserRegistrationTest(TestCase):

    def test_user_registration(self):
        # Данные для регистрации
        registration_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "Strongpassword123",
            "password2": "Strongpassword123",
        }

        # Отправка POST-запроса на регистрацию
        response = self.client.post(reverse("register"), data=registration_data)

        # Проверка, что регистрация прошла успешно и пользователя перенаправили на страницу входа
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("login"))

        # Проверка, что пользователь был создан в базе данных
        user_exists = CustomUser.objects.filter(username="testuser").exists()
        self.assertTrue(user_exists)

    def test_registration_with_mismatched_passwords(self):
        # Данные с несовпадающими паролями
        registration_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "Strongpassword123",
            "password2": "weakpassword321",
        }

        # Отправка POST-запроса на регистрацию
        response = self.client.post(reverse("register"), data=registration_data)

        # Проверка, что регистрация не удалась
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пароли не совпадают")

        # Проверка, что пользователь не был создан
        user_exists = CustomUser.objects.filter(username="testuser").exists()
        self.assertFalse(user_exists)


class UserLoginTest(TestCase):

    def setUp(self):
        # Создаем тестового пользователя
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="Strongpassword123",
        )

    def test_user_login_successful(self):
        # Данные для входа
        login_data = {
            "email": "testuser@example.com",
            "password": "Strongpassword123",
        }

        # Отправка POST-запроса на вход
        response = self.client.post(reverse("login"), data=login_data)

        # Проверка, что вход прошел успешно и пользователя перенаправили на главную страницу
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("say_hi"))

        # Проверка, что пользователь аутентифицирован
        self.assertTrue(
            self.client.login(
                email="testuser@example.com", password="Strongpassword123"
            )
        )

    def test_login_with_wrong_password(self):
        # Данные с неправильным паролем
        login_data = {
            "email": "testuser@example.com",
            "password": "wrongpassword",
        }

        # Отправка POST-запроса на вход
        response = self.client.post(reverse("login"), data=login_data)

        # Проверка, что вход не удался
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Неправильно указали пароль или почту")

        # Проверка, что пользователь не аутентифицирован
        self.assertFalse(
            self.client.login(email="testuser@example.com", password="wrongpassword")
        )
