from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.
#image title RichTextField date discription
class Blog(models.Model):
    class Meta:
        db_table = 'Blog'
        verbose_name = _('メディア記事')
        verbose_name_plural = _('メディア記事')

    title = models.CharField(verbose_name='タイトル',max_length=40,blank=True,null=False)
    image = models.ImageField(upload_to='media/',blank=True,null=False)
    body = RichTextUploadingField(blank=True,null=False)
    date = models.DateField(verbose_name='更新日',blank=True,null=False,default=timezone.now)
    discription = models.TextField(blank=True,null=False,max_length=300)
    is_public = models.BooleanField('公開する', default=False, help_text='公開する場合はチェックを入れてください')

    def __str__(self):
        template = 'タイトル：'+'{0.title}'+',　更新日：'+'{0.date}' + ', 公開状況' + '{0.is_public}'
        return template.format(self)
