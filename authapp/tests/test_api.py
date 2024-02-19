from django.contrib.auth.models import User
from django.test import TestCase
from ..api import get_user_account
import logging

logger = logging.getLogger(__name__)

class APITestCase(TestCase):
    """
    Тестирование АПИ функций приложения.
    """
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.register_data_and_email = {
            "username": "test",
            "password1": "test123123",
            "password2": "test123123",
            "email": "mail@testmail.com"
        }
        cls.register_data_no_email = {
            "username": "test",
            "password1": "test123123",
            "password2": "test123123",
        }

    def tearDown(self) -> None:
        super().tearDown()
        for user in User.objects.all():
            if user.username == "test":
                user.delete()

    def test_register_user_api_ok(self):
        """
        Тестирование создания учетной записи пользователя.
        """
        created, user, form = get_user_account(self.register_data_and_email)
        if form:
            print(f"Ошибка в данных: {form.errors}")
        self.assertTrue(
            created,
            "Аккаунт не создан!"
        )

    def test_register_user_api_error(self):
        created, user, form = get_user_account(self.register_data_no_email)
        self.assertFalse(
            created,
            "Аккаунто создан!"
        )
        self.assertIsNotNone(
            form.errors,
            "Нет словаря с ошибками!"
        )
        self.assertTrue(
            'email' in form.errors.keys(),
            "Нет адреса эл. почты!"
        )