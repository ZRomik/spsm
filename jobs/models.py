from django.db import models

class Job(models.Model):
    """
    Модель описывает должность сотрудника.
    Описание полей:
    title: CharField - название должности
    """
    title = models.CharField(max_length=100, )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Список должностей"
        db_table = "jobs"