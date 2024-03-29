# Generated by Django 3.0.8 on 2021-03-25 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0066_auto_20210312_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '利用規約・プライバシーポリシー\u3000コンテンツ', 'verbose_name_plural': '利用規約/プライバシーポリシー：コンテンツ'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '利用規約・プライバシーポリシー\u3000カテゴリー', 'verbose_name_plural': '利用規約/プライバシーポリシー：カテゴリー'},
        ),
        migrations.AlterModelOptions(
            name='chapter',
            options={'verbose_name': '利用規約・プライバシーポリシー\u3000章', 'verbose_name_plural': '利用規約/プライバシーポリシー：章'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'お問い合わせ', 'verbose_name_plural': 'お問い合わせ'},
        ),
        migrations.AlterModelOptions(
            name='major',
            options={'verbose_name': '専攻', 'verbose_name_plural': '専攻'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': 'クチコミ情報', 'verbose_name_plural': 'クチコミ情報'},
        ),
    ]
