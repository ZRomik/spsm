from jobs.models import Job
from departments.models import Department
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from ..api import get_or_create_profile
from ..models import Profile
from ..api.api_messages import *

class GetOrCreateProfileTestCase(TransactionTestCase):
    """
    Тестирование функции get_or_create_profile.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        Job.objects.get_or_create(
            title="test_job"
        )
        Department.objects.get_or_create(
            name="test_dept"
        )
        cls.test_user = User.objects.create_user(
            username="test",
            password="test"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        for j in Job.objects.all():
            j.delete()
        for d in Department.objects.all():
            d.delete()
        for p in Profile.objects.all():
            p.delete()
        cls.test_user.delete()

    def test_get_or_create_profile(self):
        created, profile, error = get_or_create_profile(
            user_pk=self.test_user.pk
        )
        self.assertTrue(
            created,
            "Флаг создания не установлен!"
        )
        self.assertIsNotNone(
            profile,
            "Профиль не создан!"
        )
        self.assertEqual(
            error,
            "",
            "Текст ошибки не пустой!"
        )
        profile.delete()

    def test_get_or_create_profile_integrity_error(self):
        created, profile, error = get_or_create_profile(
            user_pk=123
        )
        self.assertFalse(
            created,
            "Не сброшен флаг создания профиля!"
        )
        self.assertIsNone(
            profile,
            "Ссылка на профиль не пустая!"
        )
        self.assertEqual(
            ERROR_INVALID_ACCOUNT_ID,
            error,
            "Тексты ошибок не совпадают!"
        )