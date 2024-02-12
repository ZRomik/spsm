from django.urls import path
from .views import IndexPageView

app_name = "homeapp"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index")
]