from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse_lazy
from .models import Profile


class TestProfileApp(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.simple_user = User.objects.create_user(
            username="simple",
            password="simple"
        )
        cls.advanced_user = User.objects.create_user(
            username="advanced",
            password="advanced"
        )
        add_perm = Permission.objects.get(
            codename="add_profile"
        )
        cls.advanced_user.user_permissions.add(add_perm)

    @classmethod
    def tearDownClass(cls):
        cls.advanced_user.delete()

    def test_create_user_profile_without_perm(self):
        self.client.force_login(self.simple_user)
        create_url = reverse_lazy("profileapp:create", kwargs={"id": self.simple_user.id})
        response = self.client.get(create_url)
        response = self.client.post(create_url)
        self.assertEqual(
            response.status_code,
            302,
            "Неверный код ответа!"
        )

    def test_create_user_profile_with_perm(self):
        self.client.logout()
        self.client.force_login(self.advanced_user)
        create_url = reverse_lazy("profileapp:create", kwargs={"id": self.advanced_user.id})
        response = self.client.get(create_url)
        self.assertEqual(
            response.status_code,
            405,
            "Неверный код ответа GET!"
        )
        response = self.client.post(create_url)
        index_url = reverse_lazy("homeapp:index")
        self.assertRedirects(
            response,
            index_url,
            msg_prefix="Неверный редирект!"
        )
        profile = Profile.objects.get(
            user=self.advanced_user
        )
        self.assertEqual(
            type(profile),
            Profile,
            "Неверный тип объекта!"
        )
        profile.delete()