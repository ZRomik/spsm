# В этом файле находятся вспмогательные функции, необходимые для работы приложения
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def create_user(request):
    user = None
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
    return user is not None, user, form

def delete_user(user_id):
    user = User.objects.get(pk=user_id)
    user.delete()