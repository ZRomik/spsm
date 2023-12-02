from .models import Profile

def create_profile(user) -> Profile:
    return Profile.objects.create(
        user=user
    )