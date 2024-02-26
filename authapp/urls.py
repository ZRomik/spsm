from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import (
    register_user_account,
    DeleteUserAccountView,
    AccountsListView,
)


app_name = "auth"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="authapp/login.html",
            next_page="/"
        ),
        name="login"
    ),
    path(
        "logout/",
        LogoutView.as_view(
            next_page="/"
        ),
        name="logout"
    ),
    path(
        "register/",
        register_user_account,
        name="register"
    ),
    path("delete/<int:pk>/", DeleteUserAccountView.as_view(), name="delete"),
    path("accounts/", AccountsListView.as_view(), name="accounts-list")
]