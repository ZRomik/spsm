from django.urls import path
from .views import ProfileDetailView

app_name = "profileapp"
urlpatterns = [
    path("detail/<int:pk>/", ProfileDetailView.as_view(), name="detail")
]