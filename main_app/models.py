from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.

class Record(models.Model):
    class Meta:
        db_table = 'Record'
        verbose_name = _('クチコミ情報')
        verbose_name_plural = _('クチコミ情報')

    SEX_CHOICE = (
                ('man', '男性'), ('woman', '女性')
            )

    MAJOR_CHOICE = (
                ('doctor', '医師'), ('nurce', '看護師'), ('pharmacist', '薬剤師'), ('physical_therapist', '理学療法士'), ('dentist', '歯科医師'),
                ('occupational_therapist', '作業療法士'), ('registered_dietitian','管理栄養士'), ('midwife','助産師'), ('social_worker','社会福祉士'),
                ('dental_hygienist','歯科衛生士'), ('caregiver','介護士'), ('paramedic', '救急救命士'), ('psychiatric_social_worker', '精神保健福祉士'),
                ('radiation_technician','放射線検査技師'),('clinical_laboratory_technician','臨床検査技師'),('speech_language_hearing_therapist','言語聴覚士'),
                ('public_health_nurse','保健師'),('clinical_psychologist','臨床心理士'),('medical_information_manager','診療情報管理士'),('care_manager','ケアマネジャー'),
                ('orthoptist','視能訓練士'),
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
        template='{0.hospital_name} '+','+'{0.major}'+','+'{0.date}'+','+'{0.sex}'+','+'{0.year}'+','+'{0.place}'
        return template.format(self)

class Contact(models.Model):
    class Meta:
        db_table = 'Contact'
        verbose_name = _('お問い合わせ')
        verbose_name_plural = _('お問い合わせ')

    name = models.CharField(verbose_name='氏名',blank=False,null=False,max_length=100)
    email = models.EmailField(verbose_name='Email',blank=False,null=False)
    subject = models.CharField(verbose_name='タイトル',blank=False,null=False,max_length=100)
    content = models.TextField(verbose_name='お問い合わせ内容',blank=False,null=False,max_length=5000)
    date = models.DateField(verbose_name='打刻日',blank=True,null=True,default=timezone.now)

    def __str__(self):
        template='{0.date} '+','+'{0.name}'+','+'{0.subject}'
        return template.format(self)

class Major(models.Model):
    class Meta:
        db_table = 'Major'
        verbose_name = _('専攻')
        verbose_name_plural = _('専攻')

    image = models.ImageField(upload_to='media/',blank=False,null=True)
    major_name = models.CharField(verbose_name='専攻名',blank=True,null=True,max_length=100)
    db_major_name = models.CharField(verbose_name='DB用専攻名',blank=True,null=True,max_length=100)
    count = models.IntegerField(verbose_name='件数',blank=True,null=True,default=0)
    link = models.CharField(verbose_name='リンク',blank=True,null=True,max_length=100)

    def __str__(self):
        template='{0.major_name} '+','+'{0.count}'+'件'
        return template.format(self)

class Category(models.Model):
    category_tag = models.CharField(verbose_name='カテゴリー',blank=True,null=True,max_length=100)

    def __str__(self):
        return self.category_tag

    class Meta:
        verbose_name = _('利用規約・プライバシーポリシー　カテゴリー')
        verbose_name_plural = _('利用規約/プライバシーポリシー：カテゴリー')

class Chapter(models.Model):
    category_tag = models.CharField(verbose_name='カテゴリー',blank=True,null=True,max_length=100)
    chapeter_tag = models.CharField(verbose_name='条',blank=True,null=True,max_length=100)
    chapeter_name = models.CharField(blank=True,null=True,max_length=100)


    def __str__(self):
        return str(self.chapeter_tag)+'条'+':'+str(self.chapeter_name)

    class Meta:
        verbose_name = _('利用規約・プライバシーポリシー　章')
        verbose_name_plural = _('利用規約/プライバシーポリシー：章')

class Article(models.Model):
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='カテゴリー')
    article_chapter = models.ForeignKey(Chapter,blank=True,null=True, on_delete=models.CASCADE,verbose_name='章')
    article_tg = models.CharField(verbose_name='Number',blank=True,null=True,max_length=100)
    article_content = models.TextField(verbose_name='規約本文',blank=True,null=True,max_length=3000)

    def __str__(self):
        return str(self.article_category)+' '+str(self.article_chapter)+' '+str(self.article_tg)

    class Meta:
        verbose_name = _('利用規約・プライバシーポリシー　コンテンツ')
        verbose_name_plural = _('利用規約/プライバシーポリシー：コンテンツ')


class OtherRecord(models.Model):
    hospital_name = models.CharField(max_length=100,blank=True)
    username = models.CharField(max_length=100,blank=True)
    date = models.DateField(verbose_name='打刻日',blank=True,null=True,default=timezone.now)
    info = models.TextField(blank=True,null=True,max_length=3000)

    def __str__(self):
        return str(self.username) + '日付：' + str(self.date)

    class Meta:
        verbose_name = _('その他のクチコミ情報')
        verbose_name_plural = _('その他のクチコミ情報')
