from ..forms import SPSMUserCreationForm

def get_user_account(request):
    form = SPSMUserCreationForm(request)
    user = None
    if form.is_valid():
        user = form.save()
        user.email = form.cleaned_data["email"]
        user.save()
    return  user is not None, user, form if not form.is_valid() else None