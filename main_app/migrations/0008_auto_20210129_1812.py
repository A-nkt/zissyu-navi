# Generated by Django 3.0.8 on 2021-01-29 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210129_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='hospital_name',
            field=models.CharField(help_text='○○病院', max_length=100, verbose_name='病院'),
        ),
    ]
