from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .services import create_user


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