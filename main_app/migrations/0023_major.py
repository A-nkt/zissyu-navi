# Generated by Django 3.1.5 on 2021-01-30 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0022_auto_20210129_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
                ('major_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='専攻名')),
                ('count', models.IntegerField(null=True, verbose_name='件数')),
            ],
            options={
                'db_table': 'Major',
            },
        ),
    ]
