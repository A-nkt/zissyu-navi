from django.shortcuts import render
from django.http import HttpResponse
from .models import Record,Major
from .forms import RecordForm
from django_pandas.io import read_frame
import pandas as pd
import numpy as np
from django.utils import timezone

# Create your views here.
def home(request):
    datas = Record.objects.all().order_by('-date')
    datas = read_frame(datas)
    datas = datas[["hospital_name","place",'date','major']]
    datas = datas[:7]
    return render(request, 'home.html' ,{'datas': datas})

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
    MAJOR_CHOICE = (
                ('doctor', '医師'), ('nurce', '看護師'), ('pharmacist', '薬剤師'), ('physical_therapist', '理学療法士'), ('dentist', '歯科医師')
            )
    for k in range(len(MAJOR_CHOICE)):
        Major.objects.filter(db_major_name=MAJOR_CHOICE[k][0]).update(count=0)

    majors = Record.objects.all().values_list('major', flat=True).distinct() #クチコミのある職種別の参照
    #職種ごとに件数を参照して変更
    for major in majors:
        Major.objects.filter(db_major_name=major).update(count=len(Record.objects.all().filter(major=major)))
    datas = Major.objects.all()
    return render(request, 'search.html', {'datas':datas})


def list(request):
    result = pd.DataFrame()
    try:
        param = request.GET['pref']
        txt = "病院平均評価"
        datas = Record.objects.all().filter(place=param)
    except:
        param = request.GET['major']
        print(param)
        txt = "専攻平均評価"
        datas = Record.objects.all().filter(major=param)
    df_o = read_frame(datas)
    df = df_o[["hospital_name","place",'review','major']]
    dx = df[["hospital_name","place",'review','major']]
    #病院名の重複を削除 df
    for i in range(len(df)):
        if df.duplicated(subset='hospital_name')[i] == True:
            df = df.drop(index=i)
    df = df.reset_index(drop=True)
    for f in range(len(df)):
        dz = df_o
        dz = dz[["hospital_name","place",'review','major']]
        #一つの病院に限定 dz
        for j in range(len(dz)):
            if df.loc[f,'hospital_name'] != dz.loc[j,'hospital_name']:
                dz = dz.drop(index=j)
        dz = dz.reset_index(drop=True)
        #重複のある専攻を削除
        for i in range(len(dz)):
            if dz.duplicated(subset='major')[i] == True:
                dz = dz.drop(index=i)
        dz = dz.reset_index(drop=True)
        #同じ病院名において、データのある専攻を記載
        for x in range(len(dx)):
            for z in range(len(dz)):
                if dx.loc[x,'hospital_name'] == dz.loc[z,'hospital_name']:
                    dx.loc[x,'major_'+str(z)] = dz.loc[z,'major']
        result = dx
        #病院名の重複を削除 dx
        for i in range(len(result)):
            if result.duplicated(subset='hospital_name')[i] == True:
                result = result.drop(index=i)
        #スコアの導出
        result = result.reset_index(drop=True)
        for f in range(len(result)):
            score = np.zeros(0)
            for x in range(len(dx)):
                if result.loc[f,'hospital_name'] == dx.loc[x,'hospital_name']:
                    score = np.append(score, dx.loc[x,'review'])
            result.loc[f,'review'] = round(score.mean(),1)
            result.loc[f,'count'] = str(len(score))
    result = result.fillna(0)

    PLACE_CHOISE = (
                ('hokkaido', '北海道'), ('aomori', '青森'), ('iwate', '岩手'), ('akita', '秋田'),
                ('miyagi', '宮城'), ('yamagata', '山形'), ('fukushima', '福島'),('ibaraki', '茨城'),
                ('tochigi', '栃木'), ('gunma', '群馬'), ('saitama', '埼玉'), ('chiba', '千葉'),
                ('tokyo', '東京'), ('kanagawa', '神奈川'),('nigata', '新潟'), ('toyama', '富山'),
                ('ishikawa', '石川'), ('fukui', '福井'), ('yamanashi', '山梨'), ('nagano', '長野'),
                ('gihu', '岐阜'), ('shizuoka', '静岡'), ('aichi', '愛知'), ('mie', '三重'),
                ('shiga', '滋賀'), ('kyoto', '京都'), ('osaka', '大阪'), ('hyogo', '兵庫'), ('nara', '奈良'),
                ('wakayama', '和歌山'),('tottori', '鳥取'), ('simane', '島根'), ('okayama', '岡山'),
                ('hiroshima', '広島'), ('yamaguchi', '山口'), ('tokushima', '徳島'), ('kagawa', '香川'),
                ('ehime', '愛媛'), ('kochi', '高知'),('fukuoka', '福岡'), ('saga', '佐賀'), ('ohita', '大分'),
                ('miyazaki', '宮崎'), ('nagasaki', '長崎'), ('kumamoto', '熊本'), ('kagoshima', '鹿児島'), ('okinawa', '沖縄')
    )
    MAJOR_CHOICE = (
                ('doctor', '医師'), ('nurce', '看護師'), ('pharmacist', '薬剤師'), ('physical_therapist', '理学療法士'), ('dentist', '歯科医師')
            )

    for j in range(len(result)):
        for k in range(len(PLACE_CHOISE)):
            if PLACE_CHOISE[k][1] == result.loc[j,'place']:
                result.loc[j,'place_name'] = PLACE_CHOISE[k][0]

    if len(result) != 0:
        leng = len(result.loc[0])-6
        for j in range(len(result)):
            for t in range(leng):
                for x in range(len(MAJOR_CHOICE)):
                    if MAJOR_CHOICE[x][1] == result.loc[j,'major_'+str(t)]:
                        result.loc[j,'major_'+str(t)+'_name'] = MAJOR_CHOICE[x][0]
        for j in range(len(result)):
            result.loc[j,'txt'] = txt

        return render(request, 'list.html', {'result':result,'content':True,})
    else:
        #result = "コンテンツはまだありません。"
        return render(request, 'list.html', {'content':False})


def footer_content(request):
    return render(request, 'footer-content.html')

def individual(request):
    pref_query = request.GET['pref']
    hp_query = request.GET['hospital_name']
    hospital_name = hp_query #病院名
    datas = Record.objects.all().filter(place=pref_query,hospital_name=hp_query)
    df_o = read_frame(datas)

    all_count = len(df_o) #回答者数
    url = ""
    for k in range(len(df_o)):
        if df_o.loc[k,'url'] != None:
            url = df_o.loc[k,'url'] #病院URL
            url_text = "病院HP"
    if url == "":
        url_text = "公式HPは登録されていません"

    review_counter = [];review_conter_people = []
    review_counter_report = [];review_counter_communication = []
    for i in range(len(df_o)):
        review_counter.append(df_o.loc[i,'review'])
        review_conter_people.append(df_o.loc[i,'review_people'])
        review_counter_report.append(df_o.loc[i,'review_report'])
        review_counter_communication.append(df_o.loc[i,'review_communication'])
    review_average = np.mean(review_counter)
    review_average_people = np.mean(review_conter_people)
    review_average_report = np.mean(review_counter_report)
    review_average_communicaion = np.mean(review_counter_communication)

    #カテゴリ別の口コミ
    comment_people_counter = 0
    comment_report_counter = 0
    comment_communication_counter = 0
    for k in range(len(df_o)):
        if df_o.loc[k,'review_people_comment'] != '':
            comment_people_counter += 1
        if df_o.loc[k,'review_report_comment'] != '':
            comment_report_counter += 1
        if df_o.loc[k,'review_communication_comment'] != '':
            comment_communication_counter += 1
    category_count = comment_people_counter + comment_report_counter + comment_communication_counter

    df_date = Record.objects.all().filter(place=pref_query,hospital_name=hp_query).order_by('-date')
    df_date = read_frame(df_date)
    df_date = df_date[:5]
    print(df_date['review'])

    context = {
        'hospital_name':hospital_name,
        'all_count':all_count,
        'review_average':review_average,
        'review_average_people':review_average_people,
        'review_average_report':review_average_report,
        'review_average_communicaion':review_average_communicaion,
        'url':url,
        'url_text':url_text,
        'comment_people_counter':comment_people_counter,
        'comment_report_counter':comment_report_counter,
        'comment_communication_counter':comment_communication_counter,
        'category_count':category_count,
        'df_date':df_date,
    }

    return render(request, 'individual.html',context)
