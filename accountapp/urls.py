from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from .views import (
    RegisterUserView,
    ProfileDetailsView
)

app_name = "accountapp"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="accountapp/login.html", redirect_authenticated_user=True),
        name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("homeapp:index")), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("profiles/details/<int:pk>", ProfileDetailsView.as_view(), name="details")
]