# Generated by Django 3.1.5 on 2021-01-30 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_auto_20210130_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='打刻日'),
        ),
    ]
