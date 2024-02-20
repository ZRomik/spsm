from ..forms import SPSMUserCreationForm
import logging

logger = logging.getLogger(__name__)

def get_or_create_user_account(request):
    try:
        username = request.user.username
    except:
        username = "Незарегистрированный пользователь"

    logging.info(f"Обращение к АПИ.",
                 extra={
                     "username": username
                 }
                 )
    form = SPSMUserCreationForm(request.POST)
    user = None
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data["email"]
        user.save()
    return  user is not None, user, form if not form.is_valid() else None