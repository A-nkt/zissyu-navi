# Generated by Django 3.0.8 on 2021-01-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20210129_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='sex',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], null=True),
        ),
    ]
