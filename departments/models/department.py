from django.db import models

class Department(models.Model):
    """
    Модель названия рабочего отдела.
    Описание полей:
    name: CharField(100) - название отдела
    """

    name = models.CharField(max_length=100, verbose_name="Отдел")

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"
        db_table = "departments"