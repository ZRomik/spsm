from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from ..models import Profile


"""
Тестирование моделей приложения 
"""

class ProfileModelTestCase(TestCase):
    """
    Тестирование модели Profile
    """
    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create_user(
            username="user",
            password="user"
        )

    def tearDown(self) -> None:
        super().tearDown()
        self.user.delete()
        for profile in Profile.objects.all():
            profile.delete()


    def test_profile_create_profile(self):
        profile = Profile.objects.create(
            user=self.user
        )
        self.assertIsNotNone(
            profile,
            "Профиль не создан!"
        )

    def test_profile_delete_profile(self):
        profile = Profile.objects.create(
            user=self.user
        )
        profile.delete()
        with self.assertRaises(
            expected_exception=ObjectDoesNotExist,
            msg="Профиль не удален!"
        ):
            profile = Profile.objects.get(
                user=self.user
            )

    def test_profile_fio(self):
        profile = Profile.objects.create(
            user=self.user,
            lastname="Фамилия",
            firstname="имя",
            middlename="отчество"
        )
        test_fio = "Фамилия И. О."
        fio = profile.fio()
        self.assertEqual(
            fio,
            test_fio,
            "Полученная строка не совпадает с ожидаемой!"
        )