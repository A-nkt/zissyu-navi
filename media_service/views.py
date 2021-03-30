# Public Django
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from django_pandas.io import read_frame
# Public Python
import requests
#Private Django
from .models import Blog

# Create your views here.
def making_now(request):
    return render(request,'media_service/making_now.html')

@permission_required('admin.can_add_log_entry')
def main(request):
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
