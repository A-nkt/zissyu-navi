import pandas as pd
from .models import Record
from django_pandas.io import read_frame


PLACE_CHOISE = (
    ('hokkaido', '北海道'),
    ('aomori', '青森'),
    ('iwate', '岩手'),
    ('akita', '秋田'),
    ('miyagi', '宮城'),
    ('yamagata', '山形'),
    ('fukushima', '福島')
    ('ibaraki', '茨城'),
    ('tochigi', '栃木'),
    ('gunma', '群馬'),
    ('saitama', '埼玉'),
    ('chiba', '千葉'),
    ('tokyo', '東京'),
    ('kanagawa', '神奈川'),
    ('nigata', '新潟'),
    ('toyama', '富山'),
    ('ishikawa', '石川'),
    ('fukui', '福井'),
    ('yamanashi', '山梨'),
    ('nagano', '長野'),
    ('gihu', '岐阜'),
    ('shizuoka', '静岡'),
    ('aichi', '愛知'),
    ('mie', '三重'),
    ('shiga', '滋賀'),
    ('kyoto', '京都'),
    ('osaka', '大阪'),
    ('hyogo', '兵庫'),
    ('nara', '奈良'),
    ('wakayama', '和歌山'),
    ('tottori', '鳥取'),
    ('simane', '島根'),
    ('okayama', '岡山'),
    ('hiroshima', '広島'),
    ('yamaguchi', '山口'),
    ('tokushima', '徳島'),
    ('kagawa', '香川'),
    ('ehime', '愛媛'),
    ('kochi', '高知'),
    ('fukuoka', '福岡'),
    ('saga', '佐賀'),
    ('ohita', '大分'),
    ('miyazaki', '宮崎'),
    ('nagasaki', '長崎'),
    ('kumamoto', '熊本'),
    ('kagoshima', '鹿児島'),
    ('okinawa', '沖縄')
)

MAJOR_CHOICE = (
    ('doctor', '医師'),
    ('nurce', '看護師'),
    ('pharmacist', '薬剤師'),
    ('physical_therapist', '理学療法士'),
    ('dentist', '歯科医師'),
    ('occupational_therapist', '作業療法士'),
    ('registered_dietitian', '管理栄養士'),
    ('midwife', '助産師'),
    ('social_worker', '社会福祉士'),
    ('dental_hygienist', '歯科衛生士'),
    ('caregiver', '介護士'),
    ('paramedic', '救急救命士'),
    ('psychiatric_social_worker', '精神保健福祉士'),
    ('radiation_technician', '放射線検査技師'),
    ('clinical_laboratory_technician', '臨床検査技師'),
    ('speech_language_hearing_therapist', '言語聴覚士'),
    ('public_health_nurse', '保健師'),
    ('clinical_psychologist', '臨床心理士'),
    ('medical_information_manager', '診療情報管理士'),
    ('care_manager', 'ケアマネジャー'),
    ('orthoptist', '視能訓練士'),
)


def major_jp(word):
    for i in range(len(MAJOR_CHOICE)):
        if MAJOR_CHOICE[i][0] == word:
            rword = MAJOR_CHOICE[i][1]
    return rword


def inte(value):
    return '0' + str(value) if int(value) <= 9 else str(value)


def place_jp(word):
    for i in range(len(PLACE_CHOISE)):
        if PLACE_CHOISE[i][0] == word:
            rword = PLACE_CHOISE[i][1]
    return rword


def list_related_df(param):
    GROUP1 = ["北海道", "青森", "岩手", "秋田", "宮城", "山形", "福島"]
    GROUP2 = ["茨城", "栃木", "群馬", "埼玉", "千葉", "東京", "神奈川"]
    GROUP3 = ["新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜", "静岡", "三重", "愛知"]
    GROUP4 = ["滋賀", "京都", "大阪", "兵庫", "奈良", "和歌山"]
    GROUP5 = ["鳥取", "島根", "岡山", "広島", "山口", "徳島", "香川", "愛媛", "高知"]
    GROUP6 = ["福岡", "佐賀", "大分", "宮崎", "長崎", "熊本", "鹿児島", "沖縄"]
    found_ = False
    for group in GROUP1:
        if param == group:
            my_pref_group = GROUP1
            found_ = True
    if not found_:
        for group in GROUP2:
            if param == group:
                my_pref_group = GROUP2
                found_ = True
        for group in GROUP3:
            if param == group:
                my_pref_group = GROUP3
                found_ = True
        for group in GROUP4:
            if param == group:
                my_pref_group = GROUP4
                found_ = True
        for group in GROUP5:
            if param == group:
                my_pref_group = GROUP5
                found_ = True
        for group in GROUP6:
            if param == group:
                my_pref_group = GROUP6
                found_ = True
    my_pref_group.remove(param)
    group_en = []
    for pref in my_pref_group:
        for j in range(len(PLACE_CHOISE)):
            if pref == PLACE_CHOISE[j][1]:
                group_en.append(PLACE_CHOISE[j][0])

    datas = pd.DataFrame()
    for pref_en in group_en:
        datas_o = Record.objects.all().filter(place=pref_en)
        datas_o = read_frame(datas_o)
        datas = datas.append(datas_o)
    datas = datas[["hospital_name", "place", 'review']]
    datas = datas.reset_index(drop=True)

    datas_list = datas[~datas.duplicated(subset=['hospital_name', 'place'])]
    datas_list = datas_list.reset_index(drop=True)
    datas_list['review'] = 0
    datas_list['counter'] = 0

    for j in range(len(datas_list)):
        for k in range(len(datas)):
            if datas_list.loc[j, 'hospital_name'] == datas.loc[k, 'hospital_name'] and datas_list.loc[j, 'place'] == datas.loc[k, 'place']:
                datas_list.loc[j, 'review'] += datas.loc[k, 'review']
                datas_list.loc[j, 'counter'] += 1
    datas_list['average_score'] = round(datas_list['review'] / datas_list['counter'], 1)
    for k in range(len(datas_list)):
        for j in range(len(PLACE_CHOISE)):
            if datas_list.loc[k, 'place'] == PLACE_CHOISE[j][1]:
                datas_list.loc[k, 'place_name'] = PLACE_CHOISE[j][0]
    datas_list = datas_list.sort_values('counter', ascending=False)
    datas_list = datas_list[:7]
    return datas_list


def individual_related_df(pref_query, hp_query):
    for j in range(len(PLACE_CHOISE)):
        if PLACE_CHOISE[j][0] == pref_query:
            place_name = PLACE_CHOISE[j][1]

    GROUP1 = ["北海道", "青森", "岩手", "秋田", "宮城", "山形", "福島"]
    GROUP2 = ["茨城", "栃木", "群馬", "埼玉", "千葉", "東京", "神奈川"]
    GROUP3 = ["新潟", "富山", "石川", "福井", "山梨", "長野", "岐阜", "静岡", "三重", "愛知"]
    GROUP4 = ["滋賀", "京都", "大阪", "兵庫", "奈良", "和歌山"]
    GROUP5 = ["鳥取", "島根", "岡山", "広島", "山口", "徳島", "香川", "愛媛", "高知"]
    GROUP6 = ["福岡", "佐賀", "大分", "宮崎", "長崎", "熊本", "鹿児島", "沖縄"]
    found_ = False
    for group in GROUP1:
        if place_name == group:
            my_pref_group = GROUP1
            found_ = True
    if not found_:
        for group in GROUP2:
            if place_name == group:
                my_pref_group = GROUP2
                found_ = True
        for group in GROUP3:
            if place_name == group:
                my_pref_group = GROUP3
                found_ = True
        for group in GROUP4:
            if place_name == group:
                my_pref_group = GROUP4
                found_ = True
        for group in GROUP5:
            if place_name == group:
                my_pref_group = GROUP5
                found_ = True
        for group in GROUP6:
            if place_name == group:
                my_pref_group = GROUP6
                found_ = True

    group_en = []
    for pref in my_pref_group:
        for j in range(len(PLACE_CHOISE)):
            if pref == PLACE_CHOISE[j][1]:
                group_en.append(PLACE_CHOISE[j][0])

    datas = pd.DataFrame()
    for pref_en in group_en:
        datas_o = Record.objects.all().filter(place=pref_en)
        datas_o = read_frame(datas_o)
        datas = datas.append(datas_o)
    datas = datas[["hospital_name", "place", 'review']]
    datas = datas.reset_index(drop=True)
    datas_list = datas[~datas.duplicated(subset=['hospital_name', 'place'])]
    datas_list = datas_list.reset_index(drop=True)
    datas_list['review'] = 0
    datas_list['counter'] = 0

    for j in range(len(datas_list)):
        for k in range(len(datas)):
            if datas_list.loc[j, 'hospital_name'] == datas.loc[k, 'hospital_name'] and datas_list.loc[j, 'place'] == datas.loc[k, 'place']:
                datas_list.loc[j, 'review'] += datas.loc[k, 'review']
                datas_list.loc[j, 'counter'] += 1
    datas_list['average_score'] = round(datas_list['review'] / datas_list['counter'], 1)
    for k in range(len(datas_list)):
        for j in range(len(PLACE_CHOISE)):
            if datas_list.loc[k, 'place'] == PLACE_CHOISE[j][1]:
                datas_list.loc[k, 'place_name'] = PLACE_CHOISE[j][0]
    for k in range(len(datas_list)):
        if datas_list.loc[k, 'hospital_name'] == hp_query and datas_list.loc[k, 'place'] == place_name:
            datas_list = datas_list.drop(datas_list.index[k])
    datas_list = datas_list.reset_index(drop=True)

    datas_list_same_pref = pd.DataFrame(columns=['hospital_name', 'place', 'review', 'counter', 'average_score', 'place_name'])
    i = 0
    datas_list_not_pref = pd.DataFrame(columns=['hospital_name', 'place', 'review', 'counter', 'average_score', 'place_name'])
    j = 0
    for k in range(len(datas_list)):
        if datas_list.loc[k, 'place'] == place_name:
            datas_list_same_pref.loc[i] = datas_list.loc[k]
            i += 1
        else:
            datas_list_not_pref.loc[j] = datas_list.loc[k]
            j += 1
    for n in range(len(datas_list_not_pref)):
        datas_list_same_pref.loc[len(datas_list_same_pref)] = datas_list_not_pref.loc[n]
    datas_list_same_pref = datas_list_same_pref[:7]
    return datas_list_same_pref


def bottom_related_df(pref_query, hp_query, id):
    judge = False
    data_o = Record.objects.all().filter(place=pref_query, hospital_name=hp_query)
    data_o = read_frame(data_o)
    for k in range(len(data_o)):
        for j in range(len(PLACE_CHOISE)):
            if data_o.loc[k, 'place'] == PLACE_CHOISE[j][1]:
                data_o.loc[k, 'place_name'] = PLACE_CHOISE[j][0]
    for k in range(len(data_o)):
        if str(data_o.loc[k, 'id']) == id:
            data_o = data_o.drop([k])
    data_o = data_o.sort_values('year', ascending=False)
    data_o = data_o.reset_index(drop=True)
    if len(data_o) != 0:
        judge = True
    return data_o[:5], judge
