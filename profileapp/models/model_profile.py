from django.db import models
from jobs.models import Job
from departments.models import Department

class Profile(models.Model):
    """
    Модель профиля пользователя.
    fields:
    user OneToOneField: ссылка на аккаунт пользователя.
    lastname CharField: фамилия.
    firstname CharField: имя
    middlename CharField: отчество
    nmn BooleanField: отчество отсутствует.
    phone CharField: доб. ном. тел.
    mail EmailField: корп. эл. почта.
    """