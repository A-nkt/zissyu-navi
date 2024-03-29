# Generated by Django 3.0.8 on 2021-01-29 09:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0018_auto_20210129_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='review',
            field=models.IntegerField(help_text='0~5', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='実習総合評価'),
        ),
        migrations.AlterField(
            model_name='record',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='ホームページURL'),
        ),
    ]
