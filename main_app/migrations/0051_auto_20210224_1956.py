# Generated by Django 3.0.8 on 2021-02-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0050_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
