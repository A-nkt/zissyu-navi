# Generated by Django 3.1.5 on 2021-04-04 07:32

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media_service', '0002_auto_20210330_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]