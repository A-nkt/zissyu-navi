# Generated by Django 3.1.5 on 2021-04-10 02:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0067_auto_20210325_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(blank=True, max_length=100)),
                ('username', models.CharField(blank=True, max_length=100)),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='打刻日')),
                ('info', models.TextField(blank=True, max_length=3000, null=True)),
            ],
            options={
                'verbose_name': 'その他の口コミ',
                'verbose_name_plural': 'その他の口コミ',
            },
        ),
    ]