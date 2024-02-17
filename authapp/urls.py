from django.contrib.auth.views import LoginView
from django.urls import path
from .views import register_user_account

app_name = "auths"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="authapp/login.html",
            next_page="/"
        ),
        name="login"
    )
]