from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
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
        cls.register_data_ok = {
                "username": "test",
                "password1": "test123123",
                "password2": "test123123",
                "email": "mail@testmail.com"
        }
        cls.register_data_error = {
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
        factory = RequestFactory()
        request = factory.post(path="", data=self.register_data_ok)
        # request.POST = self.register_data_ok
        created, user, form = get_or_create_user_account(request)
        if form:
            for field in form:
                for error in field.errors:
                    print(f"{field.label}: {error}")
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
        request.POST = self.register_data_error
        created, user, form = get_or_create_user_account(request)
        self.assertFalse(
            created,
            "Аккаунт создан!"
        )
        self.assertIsNotNone(
            form.errors,
            "Нет словаря с ошибками!"
        )
        self.assertTrue(
            'email' in form.errors.keys(),
            "Нет адреса эл. почты!"
        )
        with self.assertRaises(
            expected_exception=ObjectDoesNotExist,
            msg="Аккаунт найден!"
        ):
            user = User.objects.get(
                username="test"
            )