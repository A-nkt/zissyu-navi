# Generated by Django 3.1.5 on 2021-02-05 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0040_auto_20210205_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_content',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='規約本文'),
        ),
    ]
