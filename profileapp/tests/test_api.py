from django.contrib.auth.models import User
from django.test import TestCase
from ..api import get_user_profile
from ..models import Profile, Avatar
"""
Тестирование вспомогательных функций приложения
"""

class GetUserProfileTestCase(TestCase):
    """
    Тестирование функции get_user_profile
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user = User.objects.create_user(
            username="test",
            password="test"
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.test_user.delete()
        for profile in Profile.objects.all():
            profile.delete()

    def test_get_user_profile_error(self):
        created, profile = get_user_profile(id = 0)
        self.assertFalse(
            created,
            "В ответе полуцчена истина!"
        )
        self.assertIsNone(
            profile,
            "Получен объект модели профиля!"
        )

    def test_get_user_profile_ok(self):
        created, profile = get_user_profile(id = self.test_user.id)
        self.assertTrue(
            created,
            "В ответе получена ложь!"
        )
        self.assertIsNotNone(
            profile,
            "Не получен объект модели профиля!"
        )