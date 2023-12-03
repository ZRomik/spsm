from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Profile
from .services import get_profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    permission_required = "profileapp.add_profile"
    queryset = Profile.objects.all().prefetch_related("avatar").prefetch_related("phones").prefetch_related("emails")
    context_object_name = "profile"

    def get(self, request, pk):
            profile = get_profile(user_id=pk)
            if profile:
                context = {
                    "profile": profile
                }
                return render(request, "profileapp/profile_detail.html", context=context)
            else:
                return HttpResponse(status=404)