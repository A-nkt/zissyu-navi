from django.contrib.sitemaps import Sitemap
from django.shortcuts import resolve_url
from media_service.models import Blog
from main_app.models import Record
from django.urls import reverse

class BlogSiteMap(Sitemap):
    """
    ブログ記事のためのサイトマップ
    """

    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Blog.objects.filter(is_public=True)


    def location(self,obj):
        return resolve_url("media_service:content_url", id=obj.id)


    def lastmod(self,obj):
        return obj.date
