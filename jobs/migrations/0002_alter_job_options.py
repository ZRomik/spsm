# Generated by Django 4.2.6 on 2024-03-04 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'Назначение', 'verbose_name_plural': 'Назначения'},
        ),
    ]