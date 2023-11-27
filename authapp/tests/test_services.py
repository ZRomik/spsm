from django.http import HttpRequest
from django.test import TestCase
from ..services import create_user

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
        self.assertIsNone(
            forms,
            "Получена форма"
        )
        user.delete()