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
    datas = Major.objects.all()

    majors = Record.objects.all().values_list('major', flat=True).distinct() #クチコミのある職種別の参照
    #職種ごとに件数を参照して変更
    for major in majors:
        Major_db = Major.objects.filter(db_major_name=major).update(count=len(Record.objects.all().filter(major=major)))
    return render(request, 'search.html', {'datas':datas})


def list(request):
    try:
        param = request.GET['pref']
    except:
        param = request.GET['major']
    datas = Record.objects.all().filter(place=param)
    return render(request, 'list.html', {'datas':datas})
