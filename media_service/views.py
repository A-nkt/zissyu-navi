from django.shortcuts import render
from django_pandas.io import read_frame
from django.db.models import Q

from .models import Blog, BlogCategory


def making_now(request):
    return render(request, 'media_service/making_now.html')


def main(request):
    context = {
        'posts': Blog.objects.filter(is_public=True).order_by('date').reverse(),
    }
    return render(request, 'media_service/main.html', context)


def content(request, id):
    if not request.user.is_staff:
        main_post = Blog.objects.get(id=id)
        main_post.views += 1
        main_post.save()

    categorys = BlogCategory.objects.all()
    for category in categorys:
        count = Blog.objects.all().filter(category=category)
        BlogCategory.objects.all().filter(category=category).update(counter=len(count))

    context = {
        'post': Blog.objects.get(id=id),
        'relations': Blog.objects.filter(~Q(id=id), is_public=True).order_by('date').reverse(),
        'ranking_post': Blog.objects.filter(~Q(id=id), is_public=True).order_by('views').reverse()[:10],
        'category': BlogCategory.objects.all(),
    }
    return render(request, 'media_service/content.html', context)


def category(request):
    category = request.GET['select']
    categorys = BlogCategory.objects.all()
    df = read_frame(categorys)
    for i in range(len(df)):
        if category == df.loc[i, 'category']:
            id = df.loc[i, 'id']
    context = {
        'posts': Blog.objects.filter(is_public=True, category=id).order_by('date').reverse(),
        'category': category,
    }
    return render(request, 'media_service/category.html', context)
