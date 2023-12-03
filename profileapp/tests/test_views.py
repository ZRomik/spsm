from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Profile

class ProfileDetailViewTestCase(TestCase):
    """
    Тестирование представления ProfileDetailView
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
        super().tearDownClass()
        cls.user.delete()
        for profile in Profile.objects.all():
            profile.delete()

    def test_profile_detail_no_logged_user(self):
        detail_url = reverse_lazy("profileapp:detail", kwargs={"pk": self.user.pk})
        response = self.client.get(detail_url)
        self.assertEqual(
            response.status_code,
            302,
            "Неверный код ответа!"
        )
        self.assertIn(
            "login",
            response.url,
            "Неверный адрес редиректа!"
        )

    def test_profile_detail_logged_user(self):
        self.client.force_login(self.user)
        detail_url = reverse_lazy("profileapp:detail", kwargs={"pk": self.user.pk})
        response = self.client.get(detail_url)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=response,
            text="Профиль",
            msg_prefix="Нет теста 'Профиль'!"
        )