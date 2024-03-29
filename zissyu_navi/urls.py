"""zissyu_navi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from main_app.sitemaps import *
from django.views.generic import TemplateView
from zissyu_navi.sitemaps import BlogSiteMap

sitemaps = {
    'BaseSitemap': BaseSitemap,
    'Post': BlogSiteMap,
}

urlpatterns = [
    path('host-admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('blog/', include('media_service.urls')),
    path('accounts/' ,include('accounts.urls')),
    path('hospee/',include('about_me.urls')),
    path('sitemap.xml', sitemap, {'sitemaps':sitemaps}, name='sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt',content_type='text/plain')),
    path('ads.txt', TemplateView.as_view(template_name='ads.txt',content_type='text/plain')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#管理者画面カスタマイズ
admin.site.site_title = 'Hospee'
admin.site.site_header = 'Hospee管理者ページ'
admin.site.index_title = 'サイトコンテンツ'
