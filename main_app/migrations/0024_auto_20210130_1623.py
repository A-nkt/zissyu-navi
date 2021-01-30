# Generated by Django 3.1.5 on 2021-01-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='リンク'),
        ),
        migrations.AlterField(
            model_name='major',
            name='image',
            field=models.ImageField(null=True, upload_to='media/images/'),
        ),
    ]
