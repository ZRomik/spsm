# Generated by Django 4.0.6 on 2024-02-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SPSM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'core',
                'permissions': [('assign_group', 'Может добавлять пользователя в группу'), ('discharge_group', 'Может удалять пользователя из группы')],
            },
        ),
    ]