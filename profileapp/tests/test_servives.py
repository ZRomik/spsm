from django.contrib.auth.models import User

from ..services import create_profile
from ..models import Profile
from django.test import TestCase

class CreateProfileTestCase(TestCase):
    """
    Тестирование функции create_profile
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
        cls.user.delete()
        for profile in Profile.objects.all():
            profile.delete()

    def test_create_profile(self):
        profile = create_profile(self.user)
        self.assertIsNotNone(
            profile,
            "Профиль не создан!"
        )