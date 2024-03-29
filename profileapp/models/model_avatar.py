from django.db import models
from .model_profile import Profile

def get_avatar_file_path(instance: "Avatar", filename: str) -> str:
    """
    Формирует путь к файлу аватара и возвращает его
    """

    if filename:
        return f"avatars/{instance.profile.pk}/{filename}"

class Avatar(models.Model):
    """
    Модель аватара профиля.
    """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="avatar")
    image = models.ImageField(upload_to=get_avatar_file_path, null=True)


    class Meta:
        db_table = "avatars"