from django.contrib.auth.models import User
from django.db import models

def get_avatar_file_path(instance: "Avatar", filename: str) -> str:
    if filename:
        return f"avatars/{instance.pk}/{filename}"

class Avatar(models.Model):
    """
    Модель описывает аватар пользователя
    """
    image = models.ImageField(upload_to=get_avatar_file_path, null=True)

    class Meta:
        db_table = "avatars"

class Phone(models.Model):
    """
    Модель описывает номер телефона
    """
    desc = models.CharField(max_length=128, null=True)
    num = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "phones"

class Email(models.Model):
    """
    Модель описывает адрес эл. почты.
    """
    desc = models.CharField(max_length=128)
    addr = models.EmailField(max_length=128)

    class Meta:
        db_table = "emails"