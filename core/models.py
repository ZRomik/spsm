from django.db import models

class SPSM(models.Model):
    class Meta:
        db_table = "core"
        permissions = [
            ("assign_group",
             "Может добавлять пользователя в группу"
             ),
            ("discharge_group",
             "Может удалять пользователя из группы"
             )
        ]