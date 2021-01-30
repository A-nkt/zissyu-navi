from django.shortcuts import render
from django.http import HttpResponse
from .models import Record,Major
from .forms import RecordForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def form(request):
    if request.method == 'POST': #POSTがされた時
        form = RecordForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = RecordForm()
            text = "投稿しました！"
            return render(request, 'form.html',{'text':text,'form':form})
    else:
        form = RecordForm()
    return render(request, 'form.html', {'form': form})


def search(request):
    datas=Major.objects.all()

    return render(request, 'search.html', {'datas':datas})


def list(request):
    try:
        param = request.GET['pref']
    except:
        param = request.GET['major']
    return render(request, 'list.html', {'param':param})
