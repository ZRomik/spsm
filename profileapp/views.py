from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Profile
@permission_required("profileapp.add_profile")
def create_user_profile_view(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == "POST":
        try:
            user = User.objects.get(pk=id)
            if user:
                profile = Profile.objects.create(
                    user=user
                )
                url = reverse_lazy("homeapp:index")
                return redirect(url)
        except Exception:
            return HttpResponse(status=404)
        return HttpResponse(status=404)
    else:
        return HttpResponse(status=405)