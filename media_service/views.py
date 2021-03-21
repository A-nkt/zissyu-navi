# Public Django
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
# Public Python
import requests
#Private Django

# Create your views here.
@permission_required('admin.can_add_log_entry')
def main(request):
    return render(request,'media_service/main.html')

def making_now(request):
    return render(request,'media_service/making_now.html')
