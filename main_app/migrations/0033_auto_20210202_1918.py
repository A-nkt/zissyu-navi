# Generated by Django 3.0.8 on 2021-02-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0032_major_db_major_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='sex',
            field=models.CharField(choices=[('man', '男性'), ('woman', '女性')], help_text='性別', max_length=100, null=True, verbose_name='性別'),
        ),
    ]