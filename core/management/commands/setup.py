from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING(
                "Первоначальная настройка сервера..."
            )
        )
        call_command(
            "create_departments_list"
        )
        call_command(
            "create_jobs_list"
        )
        self.stdout.write(
            self.style.SUCCESS(
                "Настройка завершена!"
            )
        )
