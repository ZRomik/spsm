# Generated by Django 4.2.6 on 2024-03-26 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_alter_department_options_alter_department_name'),
        ('jobs', '0004_alter_job_options'),
        ('profileapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='department', to='departments.department'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='job', to='jobs.job'),
        ),
    ]
