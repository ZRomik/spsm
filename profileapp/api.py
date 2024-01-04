from django.contrib.auth.models import User

from .models import Profile
"""
В этом файле собраны вспомогательные функции для работы приложения.
"""

def get_user_profile(id: int):
    profile = None
    try:
        user = User.objects.get(id = id)
        profile = Profile.objects.get_or_create(user = user)[0]
    except:
        pass
    return profile is not None, profile if profile else None