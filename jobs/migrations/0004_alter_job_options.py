# Generated by Django 4.2.6 on 2024-03-05 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_job_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Список должностей'},
        ),
    ]
