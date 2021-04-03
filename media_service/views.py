# Public Django
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django_pandas.io import read_frame
from django.contrib.auth.models import User
# Public Python
import requests
#Private Django
from .models import Blog

# Create your views here.
def making_now(request):
    return render(request,'media_service/making_now.html')

def main(request):
    #ユーザのログイン状態を調べる
    try:
        user = User.objects.get(username=request.user)
    except: #ユーザー認証がない時
        return redirect('/host-admin')
    context = {
        'posts':Blog.objects.all(),
    }
    return render(request,'media_service/main.html',context)

@permission_required('admin.can_add_log_entry')
def content(request,id):
    context = {
        'post':Blog.objects.get(id=id)
    }
    return render(request,'media_service/content.html',context)
