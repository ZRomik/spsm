from django.contrib.auth.models import User
from django.db import models

def get_avatar_filepath(instance: "Profile", filename: str) -> str:
    if filename:
        return f'profil/avatars/user_{instance.user.pk}/{filename}'

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # пользователь, к которму относится профиль
    firstname = models.CharField(max_length=128, null=True) # имя
    lastname = models.CharField(max_length=128, null=True) # фамилия
    middlename = models.CharField(max_length=128, null=True) # отчество
    nmn = models.BooleanField(default=False) # флаг, что отчество отсутствует
    ext_cell = models.CharField(max_length=128, null=True) # доб. тел.
    ser_cell = models.CharField(max_length=128, null=True) # служ. тел.
    pri_cell = models.CharField(max_length=128, null=True) # лич. тел.
    avatar = models.ImageField(upload_to=get_avatar_filepath, null=True)
