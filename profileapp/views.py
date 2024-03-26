from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .api import get_or_create_profile
from .models import Profile

@login_required
def view_user_profile(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Представление для визуализацми профиля пользователя.
    """
    if request.method == "GET":
        created, profile, error = get_or_create_profile(
            user_pk=pk
        )
        if created:
            context = {
                "profile": profile
            }
            return render(request, "profileapp/profile-details.html", context=context)
        else:
            errors = list(error)
            context = {
                "errors": errors
            }
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)