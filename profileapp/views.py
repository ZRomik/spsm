from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView
from .models import Profile
from .services import get_profile
from .forms import UpdateProfileForm

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

class UpdateProfileView(PermissionRequiredMixin, UpdateView):
    permission_required = "profileapp.change_profile"
    queryset = Profile.objects.all()
    form_class = UpdateProfileForm
    context_object_name = "profile"
    template_name_suffix = "_update"

    def post(self, request, *args, **kwargs):
        if "_load" in request.POST:
            pass
        elif "phone" in request.POST:
            pass
        elif "_email" in request.POST:
            pass
        elif "_save" in request.POST:
            form = UpdateProfileForm(request.POST)
            if form.is_valid():
                profile = form.save()
                url = reverse_lazy("profileapp:detail", kwargs={"pk": profile.pk})
                return redirect(url)
        else:
            return HttpResponse(status=500)