from django.contrib.auth.views import LoginView
from django.urls import path

app_name = "accountapp"

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="accountapp/login.html", redirect_authenticated_user=True),
        name="login"),
]