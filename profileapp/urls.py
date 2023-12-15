from django.urls import path
from .views import (
    ProfileDetailView,
    UpdateProfileView,
)

app_name = "profileapp"
urlpatterns = [
    path("detail/<int:pk>/", ProfileDetailView.as_view(), name="detail"),
    path("update/<int:pk>", UpdateProfileView.as_view(), name="update")
]