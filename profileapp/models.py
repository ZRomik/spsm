from django.contrib.auth.models import User
from django.db import models

def get_user_photo_path(instance: "Profile", filename: str) -> str:
    if filename:
        return f"profiles/users/{instance.user.pk}/{filename}"

class Profile(models.Model):
    firstname = models.CharField(max_length=128)
    middlename = models.CharField(max_length=128, blank=True)
    lastname = models.CharField(max_length=128)
    job = models.CharField(max_length=128, null=True)
    departmnent = models.CharField(max_length=128, null=True)
    extphone= models.CharField(max_length=128, blank=True)
    priphone = models.CharField(max_length=128, blank=True)
    serphone = models.CharField(max_length=128, blank=True)
    photo = models.ImageField(upload_to=get_user_photo_path, null=True)
    user = models.OneToOneField(User, on_delete=models.PROTECT)