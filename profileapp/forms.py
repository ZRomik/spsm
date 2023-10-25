from django import forms
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "lastname",
            "firstname",
            "middlename",
            "nmn",
            "ext_cell",
            "ser_cell",
            "pri_cell"
        ]