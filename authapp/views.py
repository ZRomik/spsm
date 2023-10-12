from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


class RegisterUserView(CreateView):
    form_class = UserCreationForm
    template_name = "authapp/register.html"
    success_url = reverse_lazy("homeapp:index")