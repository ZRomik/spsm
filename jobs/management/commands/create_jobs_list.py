from django.core.management import BaseCommand
from jobs.models import  Job


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.WARNING("Создание списка рабочих должностей...")
        )
        Job.objects.get_or_create(
            title="Программист"
        )[0].save()
        self.stdout.write(
            self.style.SUCCESS("Завершено.")
        )
