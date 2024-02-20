from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from .forms import SPSMUserCreationForm
from .api import get_or_create_user_account
from django.contrib.auth.decorators import permission_required
import logging

logger = logging.getLogger(__name__)

@permission_required("auth.add_user")
def register_user_account(request: HttpRequest) -> HttpResponse:
    logger.info(
        "Вызов register_user_account"
    )

    if request.method == "GET":
        return render(request, "authapp/register-account.html")
    elif request.method == "POST":
        created, user, form = get_or_create_user_account(request)
        if created:
            return HttpResponse("Аккаунт создан.", status=200)
        elif not created and form:
            logger.error(
                msg="Аккаунт не создан!",
                extra={
                    "username": request.user,
                    "funcame": __name__,
                }
            )
            context = {
                "form": form
            }
            return render(request, "authapp/register-account.html", context=context)
    else:
        logger.error("Тип запроса не поддерживается")
        return HttpResponse(status=405)