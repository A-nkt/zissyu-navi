# Generated by Django 3.1.5 on 2021-01-30 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_auto_20210130_1701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='time',
        ),
    ]
