from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Profile


class RegisterUserView(PermissionRequiredMixin, CreateView):
    permission_required = "add_user"

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "accountapp/register.html")

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(
                user=user
            )
            url = reverse_lazy("homeapp:index")
            return redirect(url)
        else:
            return render(request, "accountapp/register.html", context={"form": form})