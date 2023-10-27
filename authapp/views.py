from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Permission
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUserView(UserPassesTestMixin, CreateView):
    """
    Вью для регистрации аккаунта и создания профиля.
    """

    def test_func(self):
        is_staff = self.request.user.is_staff
        is_super = self.request.user.is_superuser
        user_perm = Permission.objects.get(
            codename="add_user"
        )
        profile_perm = Permission.objects.get(
            codename="add_profile"
        )
        return is_staff or is_super or (user_perm and profile_perm)

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "authapp/register.html")

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            create_profile_url = reverse_lazy("profileapp:create", kwargs={"id": user.pk})
            response = redirect(create_profile_url)
            return response
        else:
            return render(request, "authapp/register.html", context={"form": form})
