from django.contrib.auth.models import User, Permission
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

    def test_user_login(self):
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


class TestLogoutViewTestCase(TestCase):
    """
    Тестирование представления для выхода из учетной записи.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username="user",
            password="user"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.user.delete()

    def test_user_logout(self):
        self.client.force_login(self.user)
        logout_url = reverse_lazy("authapp:logout")
        response = self.client.get(logout_url)
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


class RegisterUserViewTestCase(TestCase):
    """
    Тестирование представления RegisterUserView
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )
        cls.advance_user = User.objects.create_user(
            username="advance",
            password="advance"
        )
        cls.register_data = {
            "username": "test",
            "password1": "testpass123123",
            "password2": "testpass123123"
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.simple_user.delete()
        cls.advance_user.delete()

    def setUp(self) -> None:
        super().setUp()
        add_user_perm = Permission.objects.get(
            codename="add_user"
        )
        self.advance_user.user_permissions.add(add_user_perm)
        self.advance_user.save()

    def test_register_user_by_user_no_perm(self):
        self.client.force_login(self.simple_user)
        self.assertFalse(
            self.simple_user.has_perm("auth.add_user"),
            "У пользователя есть права для регистрации!"
        )
        register_url = reverse_lazy("authapp:register")
        response = self.client.get(register_url)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=response,
            text="Вам запрещен доступ к этой странице.",
            msg_prefix="Нет сообщения об ошибке!"
        )

    def test_register_user_by_user_has_perm(self):
        self.client.force_login(self.advance_user)
        self.assertTrue(
            self.advance_user.has_perm("auth.add_user"),
            "У пользователя нет прав для регистрации!"
        )
        register_url = reverse_lazy("authapp:register")
        get_response = self.client.get(register_url)
        self.assertEqual(
            get_response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=get_response,
            text="Имя пользователя",
            msg_prefix="Нет поля 'Имя пользователя'!"
        )
        post_response = self.client.post(register_url, self.register_data)
        self.assertEqual(
            post_response.status_code,
            302,
            "Неверный код ответа!"
        )
        try:
            user = User.objects.get(
                username="test"
            )
        except Exception:
            pass
        self.assertIsNotNone(
            user,
            "Не найден созданный пользователь!"
        )
        if user:
            user.delete()