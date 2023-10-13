from django.urls import path
from .views import create_user_profile_view

app_name = "profileapp"

urlpatterns = [
    path("create/<int:id>/", create_user_profile_view, name="create")
]