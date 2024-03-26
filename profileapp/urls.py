from django.urls import path
from .views import (
    view_user_profile,
)

app_name = "profileapp"
urlpatterns = [
    path("profile/<int:pk>/", view_user_profile, name="profile"),
]