# Generated by Django 3.2.18 on 2023-04-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_remove_task_files'),
        ('packs', '0004_remove_pack_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='tasks',
        ),
        migrations.AddField(
            model_name='pack',
            name='tasks',
            field=models.ManyToManyField(related_name='task', to='tasks.Task'),
        ),
    ]