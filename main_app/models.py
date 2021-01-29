from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Record(models.Model):
    class Meta:
        db_table = 'Record'
    SEX_CHOICE = (('男', '男'), ('女', '女'))
    MAJOR_CHOICE = (('医師', '医師'), ('看護師', '看護師'), ('薬剤師', '薬剤師'), ('理学療法士', '理学療法士'), ('歯科医師', '歯科医師'))
    #PLACE_CHOISE = (('北海道', '北海道'), ('', '看護師'), ('薬剤師', '薬剤師'), ('理学療法士', '理学療法士'), ('歯科医師', '歯科医師'))

    hospital_name = models.CharField(verbose_name='病院名',max_length=100,blank=False,help_text="○○病院")
    sex = models.IntegerField(verbose_name='性別',choices=SEX_CHOICE,blank=False,null=True,help_text="性別")
    year = models.CharField(verbose_name='実習年度',max_length=100,blank=False,null=True)
    major = models.CharField(verbose_name='専攻',max_length=100,choices=MAJOR_CHOICE,blank=False,null=True,help_text="専攻")
    #place = models.CharField(verbose_name='病院所在地',max_length=100,choices=PLACE_CHOISE,blank=False,null=True,help_text="病院所在地")
    url = models.URLField(verbose_name='ホームページURL',max_length=200,blank=True,null=True)
    review = models.IntegerField(verbose_name='実習総合評価',blank=False,null=True,help_text="0~5",validators=[MinValueValidator(0),MaxValueValidator(5)])
    review_people = models.IntegerField(verbose_name='実習担当者について',blank=False,null=True,help_text="0~5",
                        validators=[MinValueValidator(0),MaxValueValidator(5)])
    review_people_comment = models.TextField(verbose_name='',blank=True,null=True,help_text="実習担当者について感じた事・思った事",max_length=1000)
    review_report = models.IntegerField(verbose_name='レポートについて',blank=False,null=True,help_text="0~5",
                        validators=[MinValueValidator(0),MaxValueValidator(5)])
    review_report_comment = models.TextField(verbose_name='',blank=True,null=True,help_text="レポートについて感じた事・思った事",max_length=1000)
    review_communication = models.IntegerField(verbose_name='コミュニケーションについて',blank=False,null=True,help_text="0~5",
                        validators=[MinValueValidator(0),MaxValueValidator(5)])
    review_communication_comment = models.TextField(verbose_name='',blank=True,null=True,help_text="コミュニケーションについて感じた事・思った事",max_length=1000)
    time = models.TimeField(verbose_name="登録時刻",blank=True,null=True)
    date = models.DateField(verbose_name='打刻日',blank=True,null=True)

    def __str__(self):
        template='{0.hospital_name} '+','+'{0.date}'+','+'{0.time}'
        return template.format(self)
