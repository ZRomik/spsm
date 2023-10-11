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

    def test_user_login(self):
        self.client.logout()
        login_url = reverse_lazy("authapp:login")
        # проверка получения страницы аутентификации
        response = self.client.get(login_url)
        self.assertEqual(
            response.status_code,
            200,
            f"Ошибка! Не удалось получить страницу аутентификации. Код {response.status_code}, ожидался код 200."
        )

        # проверка аутентификации пользователя
        response = self.client.post(
            login_url,
            data={
                "username": "simple",
                "password": "simple"
            }
        )
        self.assertEqual(
            response.status_code,
            302,
            f"Ошибка! Аутентификация пользователя не удалась. Код {response.status_code}, ожидался код 200."
        )

        home_url = reverse_lazy("homeapp:index")
        self.assertEqual(
            response.url,
            home_url,
            f"Ошибка! Выполнен редирект на страницу {response.url}, ожидля редирект на страницу {home_url}."
        )

        self.assertTrue(
            self.simple_user.is_authenticated,
            f"Ошибка! Пользователь не авторизован!"
        )

    def test_user_logout(self):
        if not self.simple_user.is_authenticated:
            self.client.force_login(self.simple_user)
        logout_url = reverse_lazy("authapp:logout")
        home_url = reverse_lazy('homeapp:index')
        response = self.client.get(logout_url)
        self.assertEqual(
            response.status_code,
            302,
            f"Ошибка! Не выполнен выход из аккаунта."
        )

        self.assertEqual(
            response.url,
            home_url,
            "Ошибка! Адрес редиректа после выхода из аккаунта не совпадает с адресом домашней страницы.."
        )