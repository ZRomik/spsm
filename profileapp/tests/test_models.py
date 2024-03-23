from jobs.models import Job
from departments.models import Department
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from ..models import Profile
from django.db.utils import IntegrityError
import logging

logger = logging.getLogger(__name__)

class ModelProfileTestCase(TransactionTestCase):
    """
    Тестирование модели :model:Profile
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user = User.objects.create_user(
            username="test",
            password="test"
        )
        Job.objects.create(
            title="job"
        )
        Department.objects.create(
            name="dept"
        )

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()
        # удаляем все профили
        if Profile.objects.count() > 0:
            for profile in Profile.objects.all():
                profile.delete()
        # удаляем все должности
        for job in Job.objects.all():
            job.delete()
        # удаляем все отделы
        for dept in Department.objects.all():
            dept.delete()
        cls.test_user.delete()

    def test_create_profile(self):
        profile = Profile.objects.create(
            user_id=self.test_user.pk
        )
        self.assertIsNotNone(
            profile,
            "Профиль не создан!"
        )
        self.assertEqual(
            profile.job,
            Job.objects.get(pk=1)
        )
        self.assertEqual(
            profile.dept,
            Department.objects.get(pk=1)
        )
        profile.delete()

    def test_create_profile_integrity_error(self):
        with self.assertRaises(
            expected_exception=IntegrityError,
            msg="Исключение не возбуждено!"
        ):
            profile = Profile.objects.create(
                user_id=self.test_user.pk
            )