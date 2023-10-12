from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy


class TestAuthApp(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )

    @classmethod
    def tearDownClass(cls):
        cls.simple_user.delete()

    def test_login_user(self):
        self.client.logout()
        login_url = reverse_lazy("authapp:login")
        home_url = reverse_lazy("homeapp:index")
        response = self.client.get(login_url)
        self.assertEqual(
            response.status_code,
            200,
            "Не получена страница логина!"
        )
        data = {
            "username": "simple",
            "password": "simple"
        }
        response = self.client.post(login_url, data)
        self.assertEqual(
            response.status_code,
            302,
            "Нет редиректа после логина!"
        )
        self.assertEqual(
            response.url,
            home_url,
            "Редирект не на домашнюю страницу!"
        )

    def test_logout_user(self):
        self.client.force_login(self.simple_user)
        logout_url = reverse_lazy("authapp:logout")
        home_url = reverse_lazy("homeapp:index")
        response = self.client.get(logout_url)
        self.assertEqual(
            response.status_code,
            302,
            "Нет редиректа после выхода из аккаунта!"
        )
        self.assertEqual(
            response.url,
            home_url,
            "Редирект не на домашнюю страницу!"
        )

    def test_register_user(self):
        self.client.logout()
        register_url = reverse_lazy("authapp:register")
        home_url = reverse_lazy("homeapp:index")
        register_data = {
            "username": "testuser",
            "password1": "testpassword123",
            "password2": "testpassword123"
        }
        get_response = self.client.get(register_url)
        self.assertEqual(
            get_response.status_code,
            200,
            "Не получена страница регистрации!"
        )
        post_response = self.client.post(register_url, register_data)
        self.assertEqual(
            post_response.status_code,
            302,
            "Нет редиректа!"
        )
        self.assertEqual(
            post_response.url,
            home_url,
            "Редирект не на домашнюю страницу!"
        )
        created_user = User.objects.get(username="testuser")
        self.assertFalse(
            created_user is None,
            "Не найден созданный аккаунт!"
        )
        created_user.delete()