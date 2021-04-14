# Generated by Django 3.0.8 on 2021-04-13 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0069_auto_20210410_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'いいね',
                'verbose_name_plural': 'いいね',
            },
        ),
        migrations.AddField(
            model_name='record',
            name='like',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.Like', verbose_name='いいね'),
        ),
    ]