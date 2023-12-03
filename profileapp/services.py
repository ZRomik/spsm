from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Profile

def get_profile(user_id: int) -> Profile:
    try:
        user = User.objects.get(pk=user_id)
        return Profile.objects.get_or_create(user=user)[0]
    except ObjectDoesNotExist as e:
        return None