from django.contrib.auth.models import User
from django.test import TransactionTestCase
from jobs.models import Job
from departments.models import Department
from ..models import Profile

class ModelProfileTestCase(TransactionTestCase):
    """
    Тестирование модели профля пользователя.
    """

    def setUp(self) -> None:
        super().setUp()
        Job.objects.get_or_create(
            title="job"
        )
        Department.objects.get_or_create(
            name="dept"
        )
        self.test_user = User.objects.create_user(
            username="test",
            password="test"
        )

    def tearDown(self) -> None:
        super().tearDown()
        self.test_user.delete()
        for job in Job.objects.all():
            job.delete()
        for dept in Department.objects.all():
            dept.delete()

    def test_create_profile_ok(self):
        profile = Profile.objects.create(
            user_id=self.test_user.pk
        )
        self.assertIsNotNone(
            profile,
            "Профиль не создан!"
        )
        if profile:
            profile.delete()