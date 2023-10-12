from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse_lazy
from .models import Profile


class TestProfileApp(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )
        cls.advance_user = User.objects.create_user(
            username="advance",
            password="advance"
        )
        cls.advance_user.is_staff = True
        add_profile_perm = Permission.objects.get(
            codename="add_profile"
        )
        if add_profile_perm:
            cls.advance_user.user_permissions.add(add_profile_perm)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.simple_user.delete()
        cls.advance_user.delete()

    def test_create_profile_without_perm(self):
        self.client.force_login(self.simple_user)
        create_url = reverse_lazy("profileapp:create", kwargs={"id": self.simple_user.id})
        response = self.client.post(create_url)
        self.assertEqual(
            response.status_code,
            302,
            "Пользователь не имеет прав на создание профиля. Не выполнен редирект!"
        )

    def test_create_profile_with_perm(self):
        self.client.force_login(self.advance_user)
        create_url = reverse_lazy("profileapp:create", kwargs={"id": self.advance_user.id})
        response = self.client.post(create_url)
        self.assertEqual(
            response.status_code,
            302,
            "Нет редиректа!"
        )
        redirect_url = reverse_lazy("homeapp:index")
        self.assertEqual(
            response.url,
            redirect_url,
            "Адрес редиректа неверный!"
        )
        profile = Profile.objects.get(user_id=self.advance_user.id)
        self.assertFalse(
            profile is None,
            "Не удалось найти созданный профиль!"
        )
        profile.delete()

    def test_create_profile_with_get_method(self):
        self.client.force_login(self.advance_user)
        create_url = reverse_lazy("profileapp:create", kwargs={"id": self.advance_user.id})
        response = self.client.get(create_url)
        self.assertEqual(
            response.status_code,
            405,
            "Выполнен запрос методом 'GET'. Получен неверный код ответа!"
        )

    def test_create_profile_without_id(self):
        self.client.force_login(self.advance_user)
        create_url = '/profile/create/'
        response = self.client.post(create_url)
        self.assertEqual(
            response.status_code,
            404,
            "Не указан id юзера. Неверный код ответа!"
        )

    def test_create_profile_with_wrong_user_id(self):
        self.client.force_login(self.advance_user)
        create_url = reverse_lazy("profileapp:create", kwargs={"id": 26})
        response = self.client.post(create_url)
        self.assertEqual(
            response.status_code,
            404,
            "Указан неверный ид юзера. Неверный код ответа!"
        )