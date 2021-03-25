from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.utils.translation import gettext as _
# Create your models here.
#image title RichTextField date discription
class Article(models.Model):
    class Meta:
        db_table = 'Article'
        verbose_name = _('メディア記事')
        verbose_name_plural = _('メディア記事')

    title = models.CharField(verbose_name='タイトル',max_length=50,blank=True,null=True)
    image = models.ImageField(upload_to='media/',blank=True,null=True)
    body = RichTextField(blank=True,null=True)
    date = models.DateField(verbose_name='更新日',blank=True,null=True,default=timezone.now)
    discription = models.TextField(blank=True,null=True,max_length=50)

    def __str__(self):
        template = '更新日：'+'{0.date} '+',　タイトル：'+'{0.title}'
        return template.format(self)
