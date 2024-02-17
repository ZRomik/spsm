from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy


class LoginViewTestCase(TestCase):
    """
    Тестирование представления для авторизации.
    """
    def setUp(self) -> None:
        super().setUp()
        self.test_user = User.objects.create_user(
            username="test",
            password="test"
        )
        self.login_data_ok = {
            "username": "test",
            "password": "test"
        }

    def tearDown(self) -> None:
        super().tearDown()
        self.test_user.delete()

    def test_user_login_ok(self):
        url = reverse_lazy("auths:login")
        response = self.client.post(
            path=url,
            data=self.login_data_ok
        )
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