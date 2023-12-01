from django.contrib.auth.models import User
from django.db import models

def get_avatar_file_path(instance: "Avatar", filename: str) -> str:
    if filename:
        return f"avatars/{instance.pk}/{filename}"

class Avatar(models.Model):
    """
    Модель описывает аватар пользователя
    """
    avatar = models.ImageField(upload_to=get_avatar_file_path, null=True)

    class Meta:
        db_table = "avatars"