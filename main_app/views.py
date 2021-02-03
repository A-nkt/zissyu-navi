from django.shortcuts import render
from django.http import HttpResponse
from .models import Record,Major
from .forms import RecordForm
from django_pandas.io import read_frame
import pandas as pd
import numpy as np
from django.utils import timezone
from django.core.paginator import Paginator
import math

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
            ('doctor', '医師'), ('nurce', '看護師'), ('pharmacist', '薬剤師'), ('physical_therapist', '理学療法士'), ('dentist', '歯科医師'),
            ('occupational_therapist', '作業療法士'), ('registered_dietitian','管理栄養士'), ('midwife','助産師'), ('social_worker','社会福祉士'),
            ('dental_hygienist','歯科衛生士'), ('caregiver','介護士'), ('paramedic', '救急救命士'), ('psychiatric_social_worker', '精神保健福祉士'),
        )

# Create your views here.
def home(request):
    datas = Record.objects.all().order_by('-date') #Recordを日付で降順
    datas = read_frame(datas) #DataFrameに格納
    datas = datas[["hospital_name","place",'date','major']] #特定のcolumnsのみ抽出
    datas = datas[:7] #最新の7項目を抽出
    #datasにplace_nameを追加
    for j in range(len(datas)):
        for k in range(len(PLACE_CHOISE)):
            if PLACE_CHOISE[k][1] == datas.loc[j,'place']:
                datas.loc[j,'place_name'] = PLACE_CHOISE[k][0]
    return render(request, 'home.html' ,{'datas': datas})

def form(request):
    if request.method == 'POST': #POSTがされた時
        form = RecordForm(request.POST)
        if form.is_valid(): #投稿されたフォームが有効だった時
            post = form.save(commit=False) #フォームを保存
            post.save()
            form = RecordForm()
            text = "投稿しました！"
            return render(request, 'form.html',{'text':text,'form':form})
    else:
        form = RecordForm()
    return render(request, 'form.html', {'form': form})


def search(request):
    #Majorに初期値0を付与
    for k in range(len(MAJOR_CHOICE)):
        Major.objects.filter(db_major_name=MAJOR_CHOICE[k][0]).update(count=0)

    majors = Record.objects.all().values_list('major', flat=True).distinct() #クチコミのある職種別の参照
    #職種ごとに件数を参照して変更
    for major in majors:
        Major.objects.filter(db_major_name=major).update(count=len(Record.objects.all().filter(major=major)))
    datas = Major.objects.all()
    return render(request, 'search.html', {'datas':datas})


def list(request):
    page = request.GET['page']
    result = pd.DataFrame()
    txt = "病院平均評価"
    try:
        param = request.GET['pref']
        param_p = "pref"
        datas = Record.objects.all().filter(place=param) #指定した都道府県の病院一覧でフィルター
        df_o = read_frame(datas)
    except:
        param = request.GET['major']
        param_p = "major"
        datas = Record.objects.all().filter(major=param) #指定した専攻でフィルター
        datas_o = read_frame(datas)
        datas_all = Record.objects.all() #全記録を取得
        datas_all = read_frame(datas_all)
        df_o = pd.DataFrame();k = 0
        datas_o = datas_o[~datas_o.duplicated(subset=['hospital_name', 'place'])] #重複を削除
        datas_o = datas_o.reset_index(drop=True)
        #病院の県と名前から記録を抽出
        for i in range(len(datas_o)):
            for j in range(len(datas_all)):
                if (datas_all.loc[j,'hospital_name'] == datas_o.loc[i,'hospital_name']) and (datas_all.loc[j,'place'] == datas_o.loc[i,'place']):
                    df_o.loc[k,'hospital_name'] = datas_all.loc[j,'hospital_name']
                    df_o.loc[k,'place'] = datas_all.loc[j,'place']
                    df_o.loc[k,'review'] = datas_all.loc[j,'review']
                    df_o.loc[k,'major'] = datas_all.loc[j,'major']
                    k += 1
    #変数定義
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
    result = result.fillna(0) #nan -> 0
    #resultにplace_nameを追加
    for j in range(len(result)):
        for k in range(len(PLACE_CHOISE)):
            if PLACE_CHOISE[k][1] == result.loc[j,'place']:
                result.loc[j,'place_name'] = PLACE_CHOISE[k][0]

    if len(result) != 0:
        leng = len(result.loc[0])-6 #majorの項目数
        for j in range(len(result)):
            for t in range(leng):
                for x in range(len(MAJOR_CHOICE)):
                    if MAJOR_CHOICE[x][1] == result.loc[j,'major_'+str(t)]:
                        result.loc[j,'major_'+str(t)+'_name'] = MAJOR_CHOICE[x][0]
        for j in range(len(result)):
            result.loc[j,'txt'] = txt
        page = int(page)
        previous_page = page - 1
        next_page = page + 1
        last_page = math.ceil(len(result) / 5)
        last_previous_page = last_page -1
        result = result[5*(page - 1):5*page]
        context = {
            'result':result,
            'content':True,
            'param':param, #pref or major
            'param_p':param_p, #pref or major
            'page':page, #今いるページ
            'previous_page':previous_page, #一個前のページ
            'next_page':next_page, #一個次のページ
            'last_page':last_page, #最後のページ
            'last_previous_page':last_previous_page,#最後の一個前
        }
        return render(request, 'list.html', context)
    else:
        return render(request, 'list.html', {'content':False})


def footer_content(request):
    return render(request, 'footer-content.html')

def individual(request):
    pref_query = request.GET['pref']
    hp_query = request.GET['hospital_name']
    hospital_name = hp_query #病院名
    datas = Record.objects.all().filter(place=pref_query,hospital_name=hp_query) #県と病院名でスクリーニング
    df_o = read_frame(datas)

    all_count = len(df_o) #回答者数
    url = ""
    for k in range(len(df_o)):
        if df_o.loc[k,'url'] != None:
            url = df_o.loc[k,'url'] #病院URL
            url_text = "病院HP"
    if url == "":
        url_text = "病院HPは登録されていません"
    #各レビューの値を計算
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

    df_date = Record.objects.all().filter(place=pref_query,hospital_name=hp_query).order_by('-date') #県と病院名でスクリーニングし、時系列方向に降順
    df_date = read_frame(df_date)
    df_date = df_date[:5] #先頭の５つを抽出

    context = {
        'hospital_name':hospital_name, #病院名
        'all_count':all_count, #回答者数
        'review_average':round(review_average,1), #総合評価
        'review_average_people':round(review_average_people,1), #実習担当者の評価
        'review_average_report':round(review_average_report,1), #レポートの評価
        'review_average_communicaion':round(review_average_communicaion,1), #コミュニケーションの評価
        'url':url, #病院HPのURLに関して
        'url_text':url_text, #URLに関するテキスト
        'comment_people_counter':comment_people_counter, #実習担当者に関する数
        'comment_report_counter':comment_report_counter, #レポートに関する数
        'comment_communication_counter':comment_communication_counter, #コミュニケーションに関する数
        'category_count':category_count, #実習担当者数+レポート数+コミュニケーション数
        'df_date':df_date,
        'pref_query':pref_query,
    }
    return render(request, 'individual.html',context)

def user_answer(request):
    id = request.GET['id']
    datas = Record.objects.all().filter(id=id);datas_o = read_frame(datas) #特定のidを抽出
    hospital_name = datas_o.loc[0,'hospital_name'];place = datas_o.loc[0,'place'] #病院名と県を取得
    #placeを元にplace_nameを決める
    for j in range(len(PLACE_CHOISE)):
        if PLACE_CHOISE[j][1] == place:
            place_name = PLACE_CHOISE[j][0]
    datas_all = Record.objects.all().filter(place=place_name,hospital_name=hospital_name) #病院名と件名から指定
    df_o = read_frame(datas_all)
    #総合評価を合計
    hospital_score = []
    for j in range(len(df_o)):
        hospital_score.append(df_o.loc[j,'review'])
    context = {
        'datas_o':datas_o,
        'hospital_name':hospital_name,
        'place':place_name,
        'length':len(datas_all),
        'score':round(np.mean(hospital_score),1),
    }
    return render(request, 'user_answer.html',context)


def user_list(request):
    pref_query = request.GET['pref']
    hp_query = request.GET['hospital_name']
    page = request.GET['page']
    try:
        about = request.GET['about']
    except:
        about = ""

    try:
        gender_query = request.GET['gender']
    except:
        gender_query = ""

    if about != "":
        if gender_query != "": #about 有,gender_query 有
            datas = Record.objects.all().filter(place=pref_query,hospital_name=hp_query,sex=gender_query)
            datas = read_frame(datas)
            if about == "people":
                for j in range(len(datas)):
                    if datas.loc[j,'review_people_comment'] == "":
                        datas = datas.drop([j])
            elif about == "report":
                for j in range(len(datas)):
                    if datas.loc[j,'review_report_comment'] == "":
                        datas = datas.drop([j])
            elif about == "communication":
                for j in range(len(datas)):
                    if datas.loc[j,'review_communication_comment'] == "":
                        datas = datas.drop([j])
            datas = datas.reset_index(drop=True)
        else: #about 有,gender_query 無
            datas = Record.objects.all().filter(place=pref_query,hospital_name=hp_query)
            datas = read_frame(datas)
            if about == "people":
                for j in range(len(datas)):
                    if datas.loc[j,'review_people_comment'] == "":
                        datas = datas.drop([j])
            elif about == "report":
                for j in range(len(datas)):
                    if datas.loc[j,'review_report_comment'] == "":
                        datas = datas.drop([j])
            elif about == "communication":
                for j in range(len(datas)):
                    if datas.loc[j,'review_communication_comment'] == "":
                        datas = datas.drop([j])
            datas = datas.reset_index(drop=True)
    else:
        if gender_query != "": #about 無,gender_query 有
            datas = Record.objects.all().filter(place=pref_query,hospital_name=hp_query,sex=gender_query)
            datas = read_frame(datas)
        else: #about 無,gender_query 無
            datas = Record.objects.all().filter(place=pref_query,hospital_name=hp_query)
            datas = read_frame(datas)

    if about == "people":
        for j in range(len(datas)):
            if datas.loc[j,'review_people_comment'] == "":
                datas = datas.drop([j])
    elif about == "report":
        for j in range(len(datas)):
            if datas.loc[j,'review_report_comment'] == "":
                datas = datas.drop([j])
    elif about == "communication":
        for j in range(len(datas)):
            if datas.loc[j,'review_communication_comment'] == "":
                datas = datas.drop([j])
    datas = datas.reset_index(drop=True)
    page = int(page)
    previous_page = page - 1
    next_page = page + 1
    last_page = math.ceil(len(datas) / 10)
    last_previous_page = last_page -1
    datas = datas.loc[10*(page-1):10*page]

    datas_all = read_frame(Record.objects.all().filter(place=pref_query,hospital_name=hp_query))
    hospital_score = []
    for j in range(len(datas_all)):
        hospital_score.append(datas_all.loc[j,'review'])

    context = {
        'datas':datas,
        'hospital_name':hp_query,
        'score':round(np.mean(hospital_score),1),
        'length':len(datas_all),
        'pref_query':pref_query,
        'place':pref_query,
        'gender_query':gender_query,
        'about':about,
        'previous_page':previous_page,
        'next_page':next_page,
        'last_previous_page':last_previous_page,
        'last_page':last_page,
        'page':page,
    }
    return render(request, 'user_list.html',context)
