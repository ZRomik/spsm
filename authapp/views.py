from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import SPSMUserCreationForm
from .api import get_user_account
from django.contrib.auth.decorators import permission_required


@permission_required("auth.add_user")
def register_user_account(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "authapp/register-account.html")
    elif request.method == "POST":
        created, user, form = get_user_account(request.POST)
        if created:
            return HttpResponse("Аккаунт создан.", status=200)
        elif not created and form:
            context = {
                "form": form
            }
            return render(request, "authapp/register-account.html", context=context)
    else:
        return HttpResponse(status=405)