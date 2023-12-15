from django import forms
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "lastname",
            "firstname",
            "middlename",
            "work_mail",
            "ext_phone",
            "work_phone",
            "self_phone"
        ]