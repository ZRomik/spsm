# Generated by Django 4.2.6 on 2024-03-04 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'db_table': 'jobs',
            },
        ),
    ]
