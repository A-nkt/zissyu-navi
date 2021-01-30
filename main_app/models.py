from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
# Create your models here.

class Record(models.Model):
    class Meta:
        db_table = 'Record'
    SEX_CHOICE = (
                ('man', '男'), ('woman', '女')
            )
    MAJOR_CHOICE = (
                ('doctor', '医師'), ('nurce', '看護師'), ('pharmacist', '薬剤師'), ('physical_therapist', '理学療法士'), ('dentist', '歯科医師')
            )
    PLACE_CHOISE = (
                ('hokkaido', '北海道'), ('aomori', '青森'), ('iwate', '岩手'), ('akita', '秋田'),
                ('miyagi', '宮城'), ('yamagata', '山形'), ('fukushima', '福島'),('ibaraki', '茨城'),
                ('tochigi', '栃木'), ('gunma', '群馬'), ('saitama', '埼玉'), ('chiba', '千葉'),
                ('tokyo', '東京'), ('kanagawa', '神奈川'),('nigata', '新潟'), ('toyama', '富山'),
                ('ishikawa', '石川'), ('fukui', '福井'), ('yamanashi', '山梨'), ('nagano', '長野'),
                ('gihu', '岐阜'), ('shizuoka', '静岡'), ('aichi', '愛知'), ('mie', '三重'),
                ('shiga', '滋賀'), ('kyoto', '京都'), ('osaka', '大阪'), ('hyogo', '兵庫'), ('nara', '奈良'),
                ('wakayama', '和歌山'),('tottori', '鳥取'), ('simane', '島根'), ('okayama', '岡山'),
                ('hiroshima', '広島'), ('yamaguchi', '山口'), ('tokushima', '徳島'), ('kagawa', '香川'),
                ('ehime', '愛媛'), ('kochi', '高知'),('fukuoka', '福岡'), ('saga', '佐賀'), ('ohita', '大分'),
                ('miyazaki', '宮崎'), ('nagasaki', '長崎'), ('kumamoto', '熊本'), ('kagoshima', '鹿児島'), ('okinawa', '沖縄')
    )

    hospital_name = models.CharField(verbose_name='病院名',max_length=100,blank=False,help_text="○○病院")
    sex = models.CharField(verbose_name='性別',choices=SEX_CHOICE,max_length=100,blank=False,null=True,help_text="性別")
    year = models.CharField(verbose_name='実習年度',max_length=100,blank=False,null=True)
    major = models.CharField(verbose_name='専攻',max_length=100,choices=MAJOR_CHOICE,blank=False,null=True,help_text="専攻")
    place = models.CharField(verbose_name='病院所在地',max_length=100,choices=PLACE_CHOISE,blank=False,null=True,help_text="病院所在地")
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
    date = models.DateField(verbose_name='打刻日',blank=True,null=True,default=timezone.now)

    def __str__(self):
        template='{0.hospital_name} '+','+'{0.date}'
        return template.format(self)


class Major(models.Model):
    class Meta:
        db_table = 'Major'

    image = models.ImageField(upload_to='media/images/',blank=False,null=True)
    major_name = models.CharField(verbose_name='専攻名',blank=True,null=True,max_length=100)
    count = models.IntegerField(verbose_name='件数',blank=False,null=True)
    link = models.CharField(verbose_name='リンク',blank=True,null=True,max_length=100)

    def __str__(self):
        template='{0.major_name} '+','+'{0.count}'+'件'
        return template.format(self)
