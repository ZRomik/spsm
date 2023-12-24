from django.contrib.auth.models import User, Permission
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

class UpdateProfileViewTestCase(TestCase):
    """
    Тестирование представления UpdateProfileView
    """
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )
        cls.advance_user = User.objects.create_user(
            username="advance",
            password="advance"
        )
        cls.profile = Profile.objects.create(user=cls.simple_user)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.advance_user.delete()
        cls.simple_user.delete()
        for profile in Profile.objects.all():
            profile.delete()

    def setUp(self) -> None:
        perm = Permission.objects.get(
            codename="change_profile"
        )
        self.advance_user.user_permissions.add(perm)
        self.advance_user.save()
        self.update_data_full = {
            "lastname": "Тестов",
            "firstname": "Тест",
            "middlename": "Тестович",
            "work_mail": "email@email.net",
            "ext_phone": "123",
            "work_phone": "123",
            "self_phone": "123",
            "_save": ""

        }

    def test_update_user_profile_by_simple_user(self):
        self.client.force_login(self.simple_user)
        update_url = reverse_lazy("profileapp:update", kwargs={"pk": self.profile.pk})
        response = self.client.get(update_url)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=response,
            text="Вам запрещен доступ к этой странице.",
            msg_prefix="Нет сообщзения о запрете доступа!"
        )

    def test_update_profile_by_advance_user(self):
        self.client.force_login(self.advance_user)
        update_url = reverse_lazy("profileapp:update", kwargs={"pk": self.profile.pk})
        response = self.client.get(update_url)
        self.assertEqual(
            response.status_code,
            200,
            "Неверный код ответа!"
        )
        self.assertContains(
            response=response,
            text="Редактирование профиля",
            msg_prefix="Нет заголовка страницы!"
        )
        response = self.client.post(
            path=update_url,
            data=self.update_data_full,
            extra="_save"

        )
        self.assertEqual(
            response.status_code,
            302,
            "Неверный код ответа!"
        )
        self.assertIn(
            "detail",
            response.url,
            "Нет строки 'detail' в адресе!"
        )