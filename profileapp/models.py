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
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="avatar", null=True)

    class Meta:
        db_table = "avatars"

class Phone(models.Model):
    """
    Модель описывает номер телефона
    """
    desc = models.CharField(max_length=128, null=True)
    num = models.CharField(max_length=128, null=True)
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE, null=True, related_name="phones")

    class Meta:
        db_table = "phones"

class Email(models.Model):
    """
    Модель описывает адрес эл. почты.
    """
    desc = models.CharField(max_length=128, null=True)
    addr = models.EmailField(max_length=128, null=True)
    profile = models.ForeignKey("Profile", null=True, related_name="emails", on_delete=models.CASCADE)

    class Meta:
        db_table = "emails"

class Profile(models.Model):
    """
    Модель описывает профиль пользователя
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    lastname = models.CharField(max_length=128, null=True, verbose_name="Фамилия")
    firstname = models.CharField(max_length=128, null=True, verbose_name="Имя")
    middlename = models.CharField(max_length=128, null=True, verbose_name="Отчество")
    nmn = models.BooleanField(default=False)
    work_mail = models.EmailField(max_length=128, null=True, blank=True, verbose_name="Раб. почта")
    ext_phone = models.CharField(max_length=128, null=True, blank=True, verbose_name="Внут. тел.")
    work_phone = models.CharField(max_length=128, null=True, blank=True, verbose_name="Служ. тел.")
    self_phone = models.CharField(max_length=128, null=True, blank=True, verbose_name="Лич. тел.")

    @property
    def fio(self):
        text = "Нет данных"
        if self.lastname:
            text = self.lastname
            if self.firstname:
                text.join([" ", self.firstname[:1], "."])
                if self.middlename:
                    text.join([" ", self.middlename[:1], "."])
        return text

    class Meta:
        db_table = "profiles"