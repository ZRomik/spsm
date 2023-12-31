from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from .views import (
    RegisterUserView,
    DeleteUserView
)

app_name = "authapp"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name = "authapp/login.html"
        ),
        name="login"
    ),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("homeapp:index")), name="logout"),
    path("register/", RegisterUserView.as_view(), name="register"),
    path("delete/<int:pk>/", DeleteUserView.as_view(), name="delete")
]