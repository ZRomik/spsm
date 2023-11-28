from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DeleteView

from .services import (
    create_user,
    delete_user
)


class RegisterUserView(PermissionRequiredMixin, View):
    permission_required = "auth.add_user"

    def get(self, request):
        return render(request, "authapp/register.html")

    def post(self, request, *args, **kwargs):
        created, user, form = create_user(request=request)
        if not created:
            context = {
                "form": form
            }
            return render(request, "authapp/register.html", context=context)
        else:
            url = reverse_lazy("homeapp:index")
            return redirect(url)

class DeleteUserView(UserPassesTestMixin, DeleteView):
    template_name = "authapp/confirm_delete_user.html"
    context_object_name = "account"
    queryset = User.objects.all()

    def test_func(self):
        is_staff = self.request.user.is_staff
        is_superuser = self.request.user.is_superuser
        has_delete_perm = self.request.user.has_perms(["auth.delete_user"])
        return is_superuser or is_staff or has_delete_perm

    def post(self, request, *args, **kwargs):
        id = kwargs["pk"]
        try:
            delete_user(user_id=kwargs["pk"])
            url = reverse_lazy("homeapp:index")
            return redirect(url)
        except ObjectDoesNotExist as e:
            context = {
                "errors": ["Учетная запись не найдена"]
            }
            return render(request, "authapp/confirm_delete_user.html", context=context)