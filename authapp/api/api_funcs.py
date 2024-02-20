from ..forms import SPSMUserCreationForm
import logging

logger = logging.getLogger(__name__)

def get_user_account(request):
    logging.info("Обращение к функции АПИ 'get_user_account'")
    form = SPSMUserCreationForm(request)
    user = None
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data["email"]
        user.save()
    return  user is not None, user, form if not form.is_valid() else None