# Generated by Django 3.1.5 on 2021-04-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_service', '0007_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]