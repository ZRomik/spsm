from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            "Настройка проекта."
        )
        self.stdout.write(
            self.style.WARNING(
                "Создание групп и разрешений..."
            )
        )
        account_manager_group = Group.objects.get_or_create(
            name="Менеджер аккаунтов"
        )[0]
        group_manager_group = Group.objects.get_or_create(
            name="Менеджер групп"
        )[0]
        role_manager_group = Group.objects.get_or_create(
            name="Менеджер назначений"
        )[0]
        add_user_perm = Permission.objects.get_or_create(
            codename="add_user"
        )[0]
        delete_user_perm = Permission.objects.get_or_create(
            codename="delete_user"
        )[0]
        auth_ct = ContentType.objects.get_for_model(
            Permission
        )
        assign_group_perm = Permission.objects.get_or_create(
            codename="assign_group",
            name="Может добавлять пользователя в группу",
            content_type=auth_ct
        )[0]
        discharge_group_perm = Permission.objects.get_or_create(
            codename="discharge_group",
            name="Может удалять пользователя из группы",
            content_type=auth_ct
        )[0]
        assign_role_perm = Permission.objects.get_or_create(
           codename="assign_role",
           name="Может назначать пользователю роль",
           content_type=auth_ct
        )[0]
        discharge_role_perm = Permission.objects.get_or_create(
            codename="discharge_role",
            name="Может отзывать у пользователя роль",
            content_type=auth_ct
        )[0]
        self.stdout.write(
            self.style.SUCCESS(
                "Завершено."
            )
        )
        self.stdout.write(
            self.style.WARNING(
                "Добавление разрешений в группы..."
            )
        )
        account_manager_group.permissions.add(
            add_user_perm
        )
        account_manager_group.permissions.add(
            delete_user_perm
        )
        account_manager_group.save()
        group_manager_group.permissions.add(
            assign_group_perm
        )
        group_manager_group.permissions.add(
            discharge_group_perm
        )
        group_manager_group.save()
        role_manager_group.permissions.add(
            assign_role_perm
        )
        role_manager_group.permissions.add(
            discharge_role_perm
        )
        role_manager_group.save()
        self.stdout.write(
            self.style.SUCCESS(
                "Завершено."
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                "Настройка завершена."
            )
        )