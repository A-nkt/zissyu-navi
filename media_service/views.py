# Public Django
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_pandas.io import read_frame
from django.contrib.auth.models import User
from django.db.models import Q
# Public Python
import requests
#Private Django
from .models import Blog,BlogCategory

# Create your views here.
def making_now(request):
    return render(request,'media_service/making_now.html')

def main(request):
    #ユーザのログイン状態を調べる
    context = {
        'posts':Blog.objects.filter(is_public=True).order_by('date').reverse(),
    }
    return render(request,'media_service/main.html',context)

def content(request,id):
    #閲覧数カウンター
    if not request.user.is_staff:
        main_post = Blog.objects.get(id=id)
        main_post.views +=1
        main_post.save()

    #カテゴリー別記事数をカウント
    categorys = BlogCategory.objects.all()
    for category in categorys:
        count = Blog.objects.all().filter(category=category)
        BlogCategory.objects.all().filter(category=category).update(counter=len(count))

    context = {
        'post':Blog.objects.get(id=id),
        'relations':Blog.objects.filter(~Q(id=id),is_public=True).order_by('date').reverse(), #最新記事
        'ranking_post':Blog.objects.filter(~Q(id=id),is_public=True).order_by('views').reverse()[:10], #人気記事 10件
        'category':BlogCategory.objects.all(),
    }
    return render(request,'media_service/content.html',context)

def category(request):
    category = request.GET['select']

    categorys = BlogCategory.objects.all()
    df = read_frame(categorys)
    for i in range(len(df)):
        if category == df.loc[i,'category']:
            id = df.loc[i,'id']

    context = {
        'posts':Blog.objects.filter(is_public=True,category=id).order_by('date').reverse(),
        'category':category,
    }
    return render(request,'media_service/category.html',context)
