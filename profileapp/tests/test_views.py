from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy
from jobs.models import Job
from departments.models import Department

from ..models import Profile
from ..api import get_or_create_profile

class ViewUserProfileTestCase(TestCase):
    """
    Тестирование представления view_user_profile
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.test_user = User.objects.create_user(
            username="test",
            password="test"
        )
        Job.objects.get_or_create(
            title="test"
        )
        Department.objects.get_or_create(
            name="test"
        )


    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.test_user.delete()
        for job in Job.objects.all():
            job.delete()
        for dept in Department.objects.all():
            dept.delete()

    def test_view_user_profile(self):
        self.client.force_login(self.test_user)
        exist, profile, error = get_or_create_profile(
            user_pk=self.test_user.pk
        )
        self.assertTrue(
            exist,
            "Профиль не создан!"
        )
        url = reverse_lazy(
            "profileapp:profile",
            kwargs={
                "pk":self.test_user.pk
            }
        )
        response = self.client.get(url)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertEqual(
            profile,
            response.context["profile"],
            "Профили не совпадают!"
        )
        if profile:
            profile.delete()