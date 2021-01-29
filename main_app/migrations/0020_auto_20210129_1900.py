# Generated by Django 3.0.8 on 2021-01-29 10:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0019_auto_20210129_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='review_report',
            field=models.IntegerField(help_text='0~5', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='レポートについて'),
        ),
        migrations.AddField(
            model_name='record',
            name='review_report_comment',
            field=models.TextField(blank=True, help_text='レポートについて感じた事・思った事', max_length=1000, null=True, verbose_name=''),
        ),
    ]
