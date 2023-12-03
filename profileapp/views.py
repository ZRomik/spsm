from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Profile
from .services import get_profile

class ProfileDetailView(LoginRequiredMixin, DetailView):
    permission_required = "profileapp.add_profile"
    queryset = Profile.objects.all()
    context_object_name = "profile"

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            profile = get_profile(user)
            if profile:
                context = {
                    "profile": profile
                }
                return render(request, "profileapp/profile_detail.html", context=context)
        except Exception as e:
            return HttpRequest(status_code=404)
