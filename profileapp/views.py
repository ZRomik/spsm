from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView

from .models import Profile

class ProfileDetailView(DetailView):
    queryset = Profile.objects.all()
    context_object_name = "profile"
    template_name_suffix = "details"
    # template_name = "profileapp/profile_detail.html"

@permission_required("profileapp.add_profile")
def create_new_profile_view(request: HttpRequest, id: int) -> HttpResponse:
    if request.method == 'GET':
        try:
            user = User.objects.get(
                pk=id
            )
        except Exception as exc:
            return HttpResponse(status=404)
        else:
            profile = Profile.objects.create(
                user=user
            )
            profile.save()
            url = reverse_lazy("profileapp:detail", kwargs={"pk": profile.pk})
            return redirect(url)
    else:
        return HttpResponse(status=405)