from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Команда для создания группы для управления разрешениями.
    """
    def handle(self, *args, **options):
        self.stdout.write("Создание группы для управления разрешениями...")
        permissions_manager_group = Group.objects.get_or_create(
            name="Менеджер разршений"
        )[0]
        assign_group_perm = Permission.objects.get(
           codename="assign_group"
        )
        discharge_group_perm = Permission.objects.get(
            codename="discharge_group"
        )
        self.stdout.write(self.style.WARNING("Добавление разрешений в группу..."))
        permissions_manager_group.permissions.add(assign_group_perm)
        permissions_manager_group.permissions.add(discharge_group_perm)
        self.stdout.write(self.style.SUCCESS("Группа создана и настроена."))
