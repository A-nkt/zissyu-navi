# Generated by Django 3.0.8 on 2021-03-25 13:04

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='タイトル')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='更新日')),
                ('discription', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'メディア記事',
                'verbose_name_plural': 'メディア記事',
                'db_table': 'Article',
            },
        ),
    ]
