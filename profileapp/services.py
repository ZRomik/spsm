from .models import Profile

def get_profile(user) -> Profile:
    return Profile.objects.get_or_create(
        user=user
    )[0]