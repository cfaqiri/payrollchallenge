# Generated by Django 4.0.2 on 2022-02-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0015_remove_employeereport_report_employeereport_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]