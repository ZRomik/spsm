from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Profile
@permission_required("profileapp.add_profile")
def create_user_profile_view(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'POST':
        if id is None:
            context = {
                "text": "Неверный формиат запроса!"
            }
            return render(request, 'profileapp/create-error-page.html', context=context, status=404)
        else:
            try:
                user = User.objects.get(pk=id)
            except Exception:
                context = {
                    "text": "Не найден аккаунт пользователя!"
                }
                return render(request, 'profileapp/create-error-page.html', context=context, status=404)
            else:
                profile = Profile.objects.create(
                    user=user
                )
                url = reverse_lazy("homeapp:index")
                return redirect(url)
    elif request.method == 'GET':
        context = {
            "text": "Неподдерживаемый запрос."
        }
        return render(request, 'profileapp/create-error-page.html', context=context, status=405)
