from django.urls import path
from .views import BasePageView

app_name = "core"
urlpatterns = [
    path("", BasePageView.as_view(), name="base")
]