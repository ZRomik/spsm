from django.contrib.auth.models import User
from django.db import models
from jobs.models import Job
from departments.models import Department

class Profile(models.Model):
    """
    Модель профиля пользователя.
    fields:
    user OneToOneField: ссылка на аккаунт пользователя.
    job :model:Job : ссылка на должность.
    dept :model:Department : ссылка на подразделение.
    lastname CharField: фамилия.
    firstname CharField: имя
    middlename CharField: отчество
    nmn BooleanField: отчество отсутствует.
    phone CharField: доб. ном. тел.
    mail EmailField: корп. эл. почта.
    """

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, related_name="profile")
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="job", null=True)
    dept = models.ForeignKey(Department, on_delete=models.PROTECT, null=True, related_name="department")
    lastname = models.CharField(max_length=128)
    firstname = models.CharField(max_length=128)
    middlename = models.CharField(max_length=128, blank=True)
    nmn = models.BooleanField(default=False)
    phone = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100)

    @property
    def fio(self):
        """
        Возвращает ФИО сотрудника
        """
        result = "Нет данных"
        if self.lastname:
            result = self.lastname.capitalize()
            if self.firstname:
                result = "".join([result, " ", self.firstname[:1].upper(), "."])
                if self.middlename and not self.nmn:
                    result = "".join([result, " ", self.middlename[:1].upper(), "."])
        return result

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if self.nmn:
            self.middlename = None
        super().save()

    class Meta:
        db_table = "profiles"