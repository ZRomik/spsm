from django.contrib.auth.models import User
from django.db import models


def get_avatar_path(instance: "Avatar", filename: str) -> str:
    if filename:
        return f"avatars/{instance.pk}/{filename}"


class Profile(models.Model):
    """
    Модель описывает профиль пользователя
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # ссылка на аккаунт пользователя
    firstname = models.CharField(max_length=128, verbose_name="Имя")  # реальное имя
    lastname = models.CharField(max_length=128, verbose_name="Фамилия")  # фамилия
    middlename = models.CharField(max_length=128, verbose_name="Отчество", null=True,
                                  blank=True)  # отчество (опционально)
    nmn = models.BooleanField(default=False, verbose_name="Нет отчества")  # флаг, что у пользователя нет отчества
    extphone = models.CharField(max_length=128, null=True, blank=True, verbose_name="Вн. тел.")  # внут. тел.
    workphone = models.CharField(max_length=128, null=True, blank=True, verbose_name="Сл. тел.")  # служ. тел.
    selfphone = models.CharField(max_length=128, null=True, blank=True, verbose_name="Лич. тел.")  # лич. тел.
    workmail = models.EmailField(max_length=128, null=True, blank=True, verbose_name="Раб. почта")  # раб. эл. почта

    def fio(self):
        text = "Нет данных"
        if self.lastname:
            text = self.lastname.capitalize()
            if self.firstname:
                text = "".join([text, " ", self.firstname[:1].upper(), "."])
                if self.middlename:
                    text = "".join([text, " ", self.middlename[:1].upper(), "."])
        return text


    class Meta:
        db_table = "profiles"


class Avatar(models.Model):
    """
    Модель описывает аватар профиля пользователя
    """
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                related_name="avatar")  # ссылка на профиль пользователя
    image = models.ImageField(null=True, upload_to=get_avatar_path)  # аватар

    class Meta:
        db_table = "avatars"
