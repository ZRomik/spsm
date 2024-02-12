from django.urls import path
from .views import AboutPageView

app_name = "aboutapp"
urlpatterns = [
    path("", AboutPageView.as_view(), name="about")
]