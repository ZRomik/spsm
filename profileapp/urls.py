from django.urls import path
from .views import (
    view_user_profile,
    change_avatar_view,
)

app_name = "profileapp"
urlpatterns = [
    path("profile/<int:pk>/", view_user_profile, name="profile"),
    path("avatar/change", change_avatar_view, name="change-avatar"),
]