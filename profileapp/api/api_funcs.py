from django.db import IntegrityError

from ..models import Profile
from .api_messages import (
    ERROR_OK,
    ERROR_INVALID_ACCOUNT_ID,
)
from .api_exceptions import ProfileApiException


def get_or_create_profile(user_pk: int = None):
    """
    Функция создает нвый профиль или находит уже созданный и возвращает его.
    """

    profile = None
    error = ERROR_OK
    try:
        if not user_pk or user_pk <= 0:
            raise ProfileApiException(ERROR_INVALID_ACCOUNT_ID)
        try:
            profile = Profile.objects.get_or_create(
                user_id=user_pk
            )[0]
        except Exception as exc:
            print(exc)
            raise ProfileApiException(ERROR_INVALID_ACCOUNT_ID)
    except ProfileApiException as exc:
        error = exc.__str__()
    finally:
        return profile is not None, profile, error
