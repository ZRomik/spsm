from django.contrib.auth.models import User
from django.test import TestCase
from ..api import get_user_profile, get_avatar
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

class GetAvatarTestCase(TestCase):
    """
    Тестирование функции get_avatar
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username="user",
            password="user"
        )
        created, cls.profile = get_user_profile(id = cls.user.id)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.profile.delete()
        cls.user.delete()
        for avatar in Avatar.objects.all():
            avatar.delete()
        for profile in Profile.objects.all():
            profile.delete()

    def test_get_avatar_error(self):
        created, avatar = get_avatar(profile=None)
        self.assertFalse(
            created,
            "В ответе получена истина!"
        )
        self.assertIsNone(
            avatar,
            "Получен объект модели аватар!"
        )

    def test_get_avatar_ok(self):
        created, avatar = get_avatar(profile=self.profile)
        self.assertTrue(
            created,
            "В ответе получена ложь!"
        )
        self.assertIsNotNone(
            avatar,
            "Не получен объект модели аватар!"
        )