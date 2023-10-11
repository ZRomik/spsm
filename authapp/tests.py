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

    def test_logout_user(self):
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

    def test_register_user(self):
        register_url = reverse_lazy("authapp:register")
        response = self.client.get(register_url)
        self.assertEqual(
            response.status_code,
            200,
            f"Ощибка! Не получена страница регистрации!"
        )
        data = {
            "username": "test",
            "password1": "test123_123",
            "password2": "test123_123"
        }
        response = self.client.post(register_url, data=data)
        self.assertEqual(
            response.status_code,
            302,
            f"Ошибка! Нет редиректа!"
        )
        home_url = reverse_lazy("homeapp:index")
        self.assertEqual(
            response.url,
            home_url,
            "Ошибка! Адреса не равны!"
        )
        user = User.objects.get(username="test")
        self.assertEqual(
            type(user),
            User,
            "Ошибка! Типы данных не равны!"
        )
        user.delete()

    def test_register_user_error(self):
        register_url = reverse_lazy("authapp:register")
        data = {
            "username": "test",
            "password1": "test123_123",
            "password2": "test123_1233"
        }
        response = self.client.post(register_url, data=data)
        self.assertEqual(
            response.status_code,
            200,
            "Получен неверный код ответа!"
        )
        print(response)
        errors = response["error"]
        print(errors)
        self.assertContains(
            response=response["errors"],
            text="errors",
            msg_prefix="Пропущена ошибка при регистрации!"
        )
