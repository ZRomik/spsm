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

    def setUp(self) -> None:
        super().setUp()
        self.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )
        Job.objects.create(title="job")
        Department.objects.create(name="dept")

    def tearDown(self) -> None:
        super().tearDown()
        for j in Job.objects.all():
            j.delete()
        for d in Department.objects.all():
            d.delete()

    def test_create_model_profile(self):
        print("job:", Job.objects.count())
        print("dept:", Department.objects.count())
        print("user:", User.objects.count())
        profile = Profile.objects.create(
            user_id=self.simple_user.pk
        )
        self.assertIsNotNone(
            profile,
            "Профиль не создан!"
        )
        profile.delete()

    def test_create_model_profile_integrity_error(self):
        with self.assertRaises(
            expected_exception=IntegrityError,
            msg="Исключение не возбуждено!"
        ):
            profile = Profile.objects.create(
                user_id=0
            )
            if profile:
                profile.delete()