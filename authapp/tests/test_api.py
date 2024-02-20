from django.contrib.auth.models import User
from django.test import RequestFactory, TestCase
from ..api import get_or_create_user_account
import logging
from django.contrib.auth.models import AnonymousUser, User

logger = logging.getLogger(__name__)

class APITestCase(TestCase):
    """
    Тестирование АПИ функций приложения.
    """
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.register_data_and_email = {
            "POST": {
                "username": "test",
                "password1": "test123123",
                "password2": "test123123",
                "email": "mail@testmail.com"
            }
        }
        cls.register_data_no_email = {
            "POST": {
                "username": "test",
                "password1": "test123123",
                "password2": "test123123",
            }
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
        factory = RequestFactory()
        request = factory.post("")
        request.POST = self.register_data_no_email
        created, user, form = get_or_create_user_account(request)
        if form:
            print(f"Ошибка в данных: {form.errors}")
        self.assertTrue(
            created,
            "Аккаунт не создан!"
        )

    def test_register_user_api_error(self):
        """
        Тестирование ошибки при регистрации аккаунта.
        """
        factory = RequestFactory()
        request = factory.post("")
        request.user = AnonymousUser
        request.POST = self.register_data_and_email
        created, user, form = get_or_create_user_account(request)
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