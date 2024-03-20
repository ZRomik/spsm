from django.core.management import BaseCommand
from departments.models import Department


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING("Создание списка подразделений...")
        )
        # Первая запись в таблице будет значением по умолчанию для профиля.
        Department.objects.get_or_create(
            name="Не указан"
        )[0].save()
        Department.objects.get_or_create(
            name="АСУ"
        )[0].save()
        self.stdout.write(
            self.style.SUCCESS("Завершено.")
        )
