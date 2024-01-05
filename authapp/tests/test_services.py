from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest
from django.test import TestCase
from ..services import (
    create_user,
    delete_user
)

class CreateUserServiceTestCase(TestCase):
    """
    Тестирование функции create_user
    """
    @classmethod
    def setUpTestData(cls):
        cls.register_data = {
            "username": "test",
            "password1": "testpass123",
            "password2": "testpass123"
        }

    def test_create_user_func(self):
        request = HttpRequest()
        request.POST = self.register_data
        created, user, forms = create_user(request)
        self.assertTrue(
            created,
            "Аккаунт не создан!"
        )
        self.assertIsNotNone(
            user,
            "Аккаунт не создан"
        )
        user.delete()

class DeleteUserServiceTestCase(TestCase):
    """
    Тестирование функции delete_user
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username="test",
            password="test"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        if cls.user:
            cls.user.delete()

    def test_delete_user_ok(self):
        delete_user(user_id=self.user.pk)
        with self.assertRaises(
            expected_exception=ObjectDoesNotExist,
            msg="Аккаунт не удален!"
        ):
            user = User.objects.get(username="test")
    def test_delete_user_error(self):
        with self.assertRaises(
                expected_exception=ObjectDoesNotExist,
                msg="Не возбудено исключение!"
        ):
            delete_user(user_id=123)