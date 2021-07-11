from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url
from media_service.models import Blog
from main_app.models import Record
from django.urls import reverse

class BlogSiteMap(Sitemap):
    """
    ブログ記事のためのサイトマップ
    """

    changefreq = "monthly" #items()の変更頻度
    priority = 0.6 #0.4~1.0の間で優先順位を決めます。デフォルトは、0.5

    def items(self): #対象とするmodelとソート・フィルター
        return Blog.objects.filter(is_public=True)

    def location(self,obj): #URLとパラメータ
        return resolve_url("media_service:content_url",id=obj.id)

    def lastmod(self,obj): #更新日
        return obj.date
