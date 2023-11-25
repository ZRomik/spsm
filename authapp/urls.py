from django.contrib.auth.views import LoginView
from django.urls import path

app_name = "authapp"
urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name = "authapp/login.html"
        ),
        name="login"
    ),
]