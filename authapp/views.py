from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import SPSMUserCreationForm
from .api import get_user_account
from django.contrib.auth.decorators import permission_required


@permission_required("auth.add_user")
def register_user_account(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        form = SPSMUserCreationForm()
        return render(request, "authapp/register-account.html", context={"form": form})
    elif request.method == "POST":
        created, user, form = get_user_account(request.POST)
        if created:
            return redirect("/")
        else:
            return HttpResponse(status=404)