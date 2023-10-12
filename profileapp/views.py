from django.contrib.auth.decorators import permission_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
@permission_required("add_profile")
def create_user_profile_view(request: HttpRequest, id: int) -> HttpResponse:
    pass