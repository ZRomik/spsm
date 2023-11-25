from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy


class LoginViewTestCase(TestCase):
    """
    Тестирование представления для аутентификации
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username="user",
            password="user"
        )
        cls.auth_data = {
            "username": "user",
            "password": "user"
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def test_login_user(self):
        self.client.logout()
        auth_url = reverse_lazy("authapp:login")
        response = self.client.post(auth_url, self.auth_data)
        self.assertEqual(
            response.status_code,
            302,
            "Неверный код ответа!"
        )
        self.assertEqual(
            response.url,
            "/",
            "Неверный адрес редиректа!"
        )