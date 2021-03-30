from django.db import models
from ckeditor.fields import RichTextField
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
    body = RichTextField(blank=True,null=False)
    date = models.DateField(verbose_name='更新日',blank=True,null=False,default=timezone.now)
    discription = models.TextField(blank=True,null=False,max_length=300)

    def __str__(self):
        template = 'タイトル：'+'{0.title}'+',　更新日：'+'{0.date}'
        return template.format(self)
