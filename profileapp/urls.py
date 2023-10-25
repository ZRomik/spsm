from django.urls import path
from .views import (
    ProfileDetailView,
    create_new_profile_view,
    UpdateProfileView,
)

app_name = "profileapp"

urlpatterns = [
    path("detail/<int:pk>/", ProfileDetailView.as_view(), name="detail"),
    path("create/<int:id>/", create_new_profile_view, name="create"),
    path("update/<int:pk>/", UpdateProfileView.as_view(), name="update"),
]