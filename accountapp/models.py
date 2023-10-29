from django.contrib.auth.models import User
from django.db import models

def get_profile_avatar_filepath(instance: "Profile", filename: str) -> str:
    if filename:
        return f"accounts/profile{instance.pk}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name="profile")
    lastname = models.CharField(max_length=128, null=True)
    firstname = models.CharField(max_length=128, null=True)
    middlename = models.CharField(max_length=128, null=True)
    nmn = models.BooleanField(default=False, null=True)
    ext_phone = models.CharField(max_length=128, null=True)
    ser_phone = models.CharField(max_length=128, null=True)
    pri_phone = models.CharField(max_length=128, null=True)
    avatar = models.ImageField(upload_to=get_profile_avatar_filepath, null=True)
    email = models.CharField(max_length=128, null=True)

    @property
    def link_str(self):
        text = 'Нет данных'
        if self.lastname:
            text = self.lastname
            if self.firstname:
                text.join([" ", self.firstname])
            if self.middlename:
                text.join([" ", self.middlename])
        return text