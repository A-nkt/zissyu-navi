# Generated by Django 3.0.8 on 2021-03-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0060_auto_20210228_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='major',
            field=models.CharField(choices=[('doctor', '医師'), ('nurce', '看護師'), ('pharmacist', '薬剤師'), ('physical_therapist', '理学療法士'), ('dentist', '歯科医師'), ('occupational_therapist', '作業療法士'), ('registered_dietitian', '管理栄養士'), ('midwife', '助産師'), ('social_worker', '社会福祉士'), ('dental_hygienist', '歯科衛生士'), ('caregiver', '介護士'), ('paramedic', '救急救命士'), ('psychiatric_social_worker', '精神保健福祉士'), ('radiation_technician', '放射線検査技師'), ('clinical_laboratory_technician', '臨床検査技師'), ('speech_language_hearing_therapist', '言語聴覚士')], help_text='専攻', max_length=100, null=True, verbose_name='専攻'),
        ),
    ]
