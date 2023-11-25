# В этом файле находятся вспмогательные функции, необходимые для работы приложения
from django.contrib.auth.forms import UserCreationForm


def create_user(request):
    user = None
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
    return user is not None, user, form if not user else None