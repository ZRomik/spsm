from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DeleteView, ListView

from .forms import SPSMUserCreationForm
from .api import get_or_create_user_account
from django.contrib.auth.decorators import permission_required
import logging

logger = logging.getLogger(__name__)

@permission_required("auth.add_user")
def register_user_account(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "authapp/register-account.html")
    elif request.method == "POST":
        created, user, form = get_or_create_user_account(request)
        if created:
            return HttpResponse("Аккаунт создан.", status=200)
        elif not created and form:
            logger.info(
                msg="Аккаунт не создан!",
                extra={
                    "username": request.user.username
                }
            )
            context = {
                "form": form
            }
            return render(request, "authapp/register-account.html", context=context)
    else:
        logger.warning(
            f"получен неподдерживаемый запрос {request.method}.",
            extra={
                "username": request.user.username
            }
        )
        return HttpResponse(status=405)

class DeleteUserAccountView(PermissionRequiredMixin, DeleteView):
    permission_required = "auth.delete_user"
    template_name = "authapp/confirm-account-delete.html"
    queryset = User.objects.all()
    context_object_name = "usr"
    success_url = "/"

class AccountsListView(LoginRequiredMixin, ListView):
    template_name = "authapp/accounts-list.html"
    model = User
    queryset = User.objects.all()
    context_object_name = "users"