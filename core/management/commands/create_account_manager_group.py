from django.contrib.auth.models import Permission, Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    """
    Команда для создания группы для работы с учетной записью пользователя.
    """
    def handle(self, *args, **options):
        self.stdout.write("Создание и настройка группы для работы с учетной записью пользователя.")
        account_manager_group = Group.objects.get_or_create(
            name="Менеджер учетных записей"
        )[0]
        add_user_perm = Permission.objects.get(
            codename="add_user"
        )
        delete_user_perm = Permission.objects.get(
            codename="delete_user"
        )
        self.stdout.write(self.style.WARNING("Добавление разрешений..."))
        account_manager_group.permissions.add(add_user_perm)
        account_manager_group.permissions.add(delete_user_perm)
        self.stdout.write(self.style.SUCCESS("Группа создана и настроена."))
