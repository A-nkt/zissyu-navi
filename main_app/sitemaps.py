from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class BaseSitemap(Sitemap):
    #静的ページのサイトマップ
    changefreq = "never"
    priority = 0.9

    def items(self):
        context = [
            'main_app:home','main_app:form','main_app:search','main_app:list',
            'main_app:footer_content','main_app:individual','main_app:user_answer',
            'main_app:user_list','main_app:contact']
        return context

    def location(self, item):
        return reverse(item)
