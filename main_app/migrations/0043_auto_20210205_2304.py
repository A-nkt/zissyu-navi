# Generated by Django 3.1.5 on 2021-02-05 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0042_auto_20210205_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_chapter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.chapter', verbose_name='章'),
        ),
    ]
