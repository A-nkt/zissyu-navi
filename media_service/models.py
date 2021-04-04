from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.
class BlogCategory(models.Model):
    class Meta:
        db_table = 'BlogCategory'
        verbose_name = _('記事カテゴリー')
        verbose_name_plural = _('記事カテゴリー')

    category = models.CharField(max_length=100)
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        template = '{0.category}'
        return template.format(self)


class Blog(models.Model):
    class Meta:
        db_table = 'Blog'
        verbose_name = _('メディア記事')
        verbose_name_plural = _('メディア記事')

    title = models.CharField(verbose_name='タイトル',max_length=40,blank=True,null=False)
    category = models.ForeignKey(BlogCategory,blank=True,null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/',blank=True,null=False)
    body = RichTextUploadingField(blank=True,null=False)
    date = models.DateField(verbose_name='更新日',blank=True,null=False,default=timezone.now)
    discription = models.TextField(blank=True,null=False,max_length=300)
    is_public = models.BooleanField('公開する', default=False, help_text='公開する場合はチェックを入れてください')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        template = 'タイトル：'+'{0.title}'+',　更新日：'+'{0.date}' + ', 公開状況：' + '{0.is_public}'
        return template.format(self)
