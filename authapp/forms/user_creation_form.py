from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SPSMUserCreationForm(UserCreationForm):
    """
    Форма для создания ученой записи пользователя.
    """
    email = forms.CharField(label="Эл. почта", required=True)
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "email",
        ]

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user