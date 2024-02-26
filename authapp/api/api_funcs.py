from ..forms import SPSMUserCreationForm
import logging
from core.helpers.log_helpers import get_username

logger = logging.getLogger(__name__)

def get_or_create_user_account(request):
    form = SPSMUserCreationForm(request.POST)
    user = None
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data["email"]
        user.save()
    else:
        logger.warning(
            "Не удалось создать аккаунт. Ошибка в  полученных данных.",
            extra={
                "username": get_username(request)
            }
        )
    return  user is not None, user, form if not user else None