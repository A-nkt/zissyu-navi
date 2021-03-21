# Public Django
from django.shortcuts import render
# Public Python
import requests
#Private Django

# Create your views here.
def main(request):
    return render(request,'media_service/main.html')

def making_now(request):
    return render(request,'media_service/making_now.html')
