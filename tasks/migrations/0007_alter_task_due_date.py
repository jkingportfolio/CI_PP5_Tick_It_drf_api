# Generated by Django 3.2.18 on 2023-04-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20230406_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default='No due date', null=True),
        ),
    ]
