# Generated by Django 3.2.18 on 2023-04-16 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packs', '0003_alter_pack_pack_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pack',
            name='members',
        ),
    ]
