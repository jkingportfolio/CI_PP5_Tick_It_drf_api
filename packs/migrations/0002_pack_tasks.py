# Generated by Django 3.2.18 on 2023-03-17 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20230316_1534'),
        ('packs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pack',
            name='tasks',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='task', to='tasks.task'),
            preserve_default=False,
        ),
    ]