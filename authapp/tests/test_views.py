from django.contrib.auth.models import User, Group, Permission
from django.core.exceptions import ObjectDoesNotExist
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
        self.login_data_error = {
            "username": "user",
            "password": "user"
        }

    def tearDown(self) -> None:
        super().tearDown()
        self.test_user.delete()

    def test_user_login_ok(self):
        url = reverse_lazy("auth:login")
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

    def test_user_login_error(self):
        url = reverse_lazy("auth:login")
        response = self.client.post(url, self.login_data_error)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный адоес редиректа."
        )
        self.assertContains(
            response=response,
            text="Исправьте перечисленные ошибки.",
            msg_prefix="Нет заголовка списка ошибок!"
        )

class LogoutViewTestCase(TestCase):
    """
    Тестирование представления для выхода из аккаунта.
    """
    def setUp(self) -> None:
        super().setUp()
        self.test_user = User.objects.create_user(
            username="test",
            password="test"
        )

    def tearDown(self) -> None:
        super().tearDown()
        self.test_user.delete()

    def test_logout_user_ok(self):
        self.client.force_login(self.test_user)
        url = reverse_lazy("auth:logout")
        response = self.client.get(url)
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

class RegisterUserAccountTestCase(TestCase):
    """
    Тестирование представления для регистрации аккаунта.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.creator = User.objects.create_user(
            username="creator",
            password="creator"
        )
        cls.group = Group.objects.create(name="test-group"
                                          )
        add_user_perm = Permission.objects.get(
            codename="add_user"
        )
        cls.group.permissions.add(add_user_perm)
        cls.group.save()
        cls.creator.groups.add(cls.group)
        cls.creator.save()
        cls.register_data_ok = {
            "username": "simpleuser",
            "password1": "simplepass123",
            "password2": "simplepass123",
            "email": "simple@mail.net"
        }

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.creator.delete()
        cls.group.delete()
        try:
            user = User.objects.get(
                username="simpleuser"
            )
            if user:
                user.delete()
        except:
            pass

    def test_register_user_view_ok(self):
        self.client.force_login(self.creator)
        url = reverse_lazy("auth:register")
        response = self.client.post(url, self.register_data_ok)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=response,
            text="Аккаунт создан.",
            msg_prefix="Нет сообщения о создании аккаунта!"
        )
        try:
            simple_user = User.objects.get(
                username="simpleuser"
            )
        except:
            pass
        self.assertIsNotNone(
            simple_user,
            "Аккаунт не найден!"
        )
        simple_user.delete()

    def test_register_user_view_error_405(self):
        self.client.force_login(self.creator)
        url = reverse_lazy("auth:register")
        response = self.client.put(
            path=url,
            extra=self.register_data_ok
        )
        self.assertEqual(
            response.status_code,
            405,
            "Неверный код ответа!"

        )

class DeleteUserAccountTestCase(TestCase):
    """
    Тестировани епредставления DeleteUserAccountView
    """
    def setUp(self) -> None:
        super().setUp()
        self.test_user = User.objects.create_user(
            username="test",
            password="test"
        )
        self.user = User.objects.create_user(
            username="user",
            password="user"
        )
        self.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )
        self.group = Group.objects.get_or_create(
            name="test_group"
        )[0]
        delete_user_perm = Permission.objects.get(
            codename="delete_user"
        )
        self.group.permissions.add(delete_user_perm)
        self.group.save()
        self.user.groups.add(self.group)
        self.user.save()

    def tearDown(self) -> None:
        super().tearDown()
        self.user.delete()
        self.simple_user.delete()
        self.group.delete()
        try:
            self.test_user.delete()
        except:
            pass

    def test_delete_user_account_no_perm_user(self):
        self.client.force_login(self.test_user)
        self.assertFalse(
            self.test_user.groups.filter(name="simple_group").exists(),
            "У пользователя есть права на удаление аккаунта!"

        )
        url = reverse_lazy("auth:delete", kwargs={"pk": self.test_user.pk})
        response = self.client.post(url)
        self.assertEqual(
            response.status_code,
            403,
            "Неверный код ответа!"
        )

    def test_delete_user_account_perm_user(self):
        self.client.force_login(self.user)
        self.assertTrue(
            self.user.groups.filter(name="test_group").exists(),
            "У пользователя нет прав на удаление аккаунта!"
        )
        url = reverse_lazy("auth:delete", kwargs={"pk": self.test_user.pk})
        response = self.client.post(url)
        self.assertEqual(
            response.status_code,
            302,
            "Неверный код ответа!"
        )
        self.assertIn(
            response.url,
            "/",
            "Неверный адрес редиректа!"
        )
        with self.assertRaises(
            expected_exception=ObjectDoesNotExist,
            msg="Аккаунт не удален!"
        ):
            user = User.objects.get(
                username="test"
            )

class AccountsListViewTestCase(TestCase):
    """
    Тестирование представления AccountsListView
    """
    def setUp(self) -> None:
        super().setUp()
        self.test_user = User.objects.create_user(
            username="test",
            password="test"
        )

    def tearDown(self) -> None:
        super().tearDown()
        self.test_user.delete()

    def test_accounts_list_no_logged_user(self):
        self.client.logout()
        url = reverse_lazy("auth:accounts-list")
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            302,
            "Неверный код ответа!"
        )
        self.assertIn(
            "login",
            response.url,
            "Неверный адрес редиректа!"
        )