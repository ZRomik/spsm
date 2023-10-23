from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse_lazy
from profileapp.models import Profile


class TestAuthapp(TestCase):
    """
    Тестирование функционала приложения.
    """
    register_data = {
        "username": "testuser",
        "password1": "testpassword123",
        "password2": "testpassword123",
    }
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
        add_user_perm = Permission.objects.get(
            codename="add_user"
        )
        add_profile_perm = Permission.objects.get(
            codename="add_profile"
        )
        cls.advance_user.user_permissions.add(
            add_user_perm, add_profile_perm,
                                              )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.advance_user.delete()
        cls.simple_user.delete()

    def test_register_user_by_no_logged_user(self):
        self.client.logout()
        register_url = reverse_lazy("authapp:register")
        response = self.client.get(register_url)
        self.assertEqual(
            response.status_code,
            302,
            "Нет редиректа!"
        )
        self.assertIn(
            "login",
            response.url,
            "В адресе ответа нет строки 'login'!"
        )

    def test_register_user_by_simple_user(self):
        self.client.force_login(self.simple_user)
        register_url = reverse_lazy("authapp:register")
        get_response = self.client.get(register_url)
        self.assertEqual(
            get_response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=get_response,
            text="403",
            msg_prefix="Отсутствует код ошибки '403'!"
        )
        post_response = self.client.post(
            register_url,
            data=self.register_data
        )
        self.assertEqual(
            post_response.status_code,
            200,
            "Страница не получена!"
        )
        self.assertContains(
            response=get_response,
            text="403",
            msg_prefix="Отсутствует код ошибки '403'!"
        )

    def test_register_user_by_advance_user(self):
        self.client.force_login(self.advance_user)
        register_url = reverse_lazy("authapp:register")
        get_response = self.client.get(register_url)
        self.assertEqual(
            get_response.status_code,
            200,
            "Не получена страница регистрации!"
        )
        self.assertNotContains(
            response=get_response,
            text="403",
            msg_prefix="Обнаружен код ошибки '403'!"
        )
        post_response = self.client.post(register_url, data=self.register_data)
        self.assertEqual(
            post_response.status_code,
            302,
            f"Неверный код ответа {post_response.status_code}"
        )
        created_user = User.objects.get(username="testuser")
        self.assertEqual(
            type(created_user),
            User,
            "Тип объекта не идентичен типу модели!"
        )