# Generated by Django 3.0.8 on 2021-02-24 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0051_auto_20210224_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]