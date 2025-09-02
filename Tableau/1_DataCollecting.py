from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

select_date = [None, 'month', '3months', '6months', 'year']
position = ['TANK', 'DAMAGE', 'SUPPORT']

tank_set = set(['D.VA', 'REINHARDT', 'ZARYA', 'ROADHOG', 'ORISA', 'WINSTON', 'SIGMA', 'WRECKING BALL', 'JUNKER QUEEN', 'DOOMFIST', 'RAMATTRA', 'MAUGA'])
dealer_set = set(['CASSIDY', 'SOLDIER: 76', 'GENJI', 'ASHE', 'HANZO', 'WIDOWMAKER', 'JUNKRAT', 'TRACER', 'SOMBRA', 'PHARAH', 'MEI', 'REAPER', 'SOJOURN', 'BASTION', 'TORBJÖRN', 'SYMMETRA', 'VENTURE', 'ECHO'])
healer_set = set(['ANA', 'MERCY', 'MOIRA', 'ZENYATTA', 'KIRIKO', 'JUNO', 'LÚCIO', 'LIFEWEAVER', 'BAPTISTE', 'BRIGITTE', 'ILLARI'])

while(True):
    input_data = int(input('DF으로 추출할 날짜 선택 \n [0 -> 종료] \n [1 -> 현재] \n [2 -> 3달 전] \n [3 -> 6달 전] \n [4 ->12달 전] \n'))

    if input_data == 0:
        break

    html_contents = None
    date = select_date[input_data]

    with open(f'Tableau/html_parser/owbuff_{date}_overview.html', 'r', encoding='utf-8') as f:
        html_contents = f.read()

    soup = BeautifulSoup(html_contents, 'html.parser')

    #- 1-1. Overview 파트 col 추출
    tmp = soup.find_all('div', class_='group inline-flex items-center whitespace-nowrap pointer-events-auto cursor-pointer select-none')
    col_lst = []

    for col in tmp:
        col = col.text
        col = str(col).replace('\n', '')
        col = col.strip()

        if col not in col_lst:
            col_lst.append(col)

    print(col_lst) #- Hero / Win Rate / KDA (추가완료)
        #- Primary: ELIMS / DAMAGE / HEALING
        #- Eliminations: SOLO KILLS / FINAL BLOWS

    #- 1-2. 영웅 이름(Hero) 추출
    tmp = soup.find_all(class_='font-semibold uppercase whitespace-nowrap')
    hero_name_lst = []
    for hero_name in tmp:
        hero_name = hero_name.text
        hero_name = str(hero_name).replace('\n', '')
        hero_name = hero_name.strip()

        if hero_name not in hero_name_lst:
            hero_name_lst.append(hero_name)

    print(len(hero_name_lst))

    #- 1-3. 픽률(Pick Rate) / 승률(Win Rate) / 킬뎃(KDA) 추출
    tmp = soup.find_all('td', class_='py-2 px-2 sm:first:px-4 sm:last:px-4')
    overview_lst = []
    three_pair = []
    for data in tmp:
        data = data.text
        data = str(data).replace('\n', '')
        data = str(data).replace('%', '')
        data = data.strip()

        if data == '': #아무것도 없는 경우
            continue

        three_pair.append(data)

        if len(three_pair) == 3: #3개 -> 픽률, 승률, 킬뎃
            overview_lst.append(three_pair.copy())
            three_pair.clear()

    print(overview_lst)
    print(len(overview_lst))
    print()

    #- 2-1. Primary html
    with open(f'Tableau/html_parser/owbuff_{date}_Primary.html', 'r' ,encoding='utf-8') as f:
        html_contents = f.read()

    soup = BeautifulSoup(html_contents, 'html.parser')

    #- 2-2. 열 이름 추출 - ELIMS / DAMAGE / HEALING
    tmp = soup.find_all(class_='inline-flex flex-nowrap justify-start items-end gap-0.5')
    primary_col_lst = []
    for data in tmp:
        data = str(data.text)
        data = data.replace('\n', '')
        data = data.strip()
        data = data.split('/')[0]
        col_name = data.strip()

        if col_name not in primary_col_lst:
            primary_col_lst.append(col_name)

    print(f'primary 열 이름 리스트: {primary_col_lst}') #- 여기서 나는 ELIMS / DAMAGE / HEALING 부분만 사용할 예정

    #- 2-3. 데이터 추출 - ELIMS / DAMAGE / HEALING
    tmp = soup.find_all('td', class_='py-2 px-2 sm:first:px-4 sm:last:px-4')
    primary_data_lst = []
    pair_five = []
    for data in tmp:
        data = str(data.text)
        data = data.replace('\n', '')
        data = data.strip()
        
        try:
            pair_five.append(float(data))

        except ValueError as e:
            pair_five.append(data)

        if len(pair_five) == 5:
            primary_data_lst.append(pair_five.copy())
            pair_five.clear()

    print(f'primary data 수치: {primary_data_lst}')
    print(f'primary data 총 갯수: {len(primary_data_lst)}')
    
    #- 3-1. Eliminations html
    with open(f'Tableau/html_parser/owbuff_{date}_Eliminations.html', 'r' ,encoding='utf-8') as f:
        html_contents = f.read()

    soup = BeautifulSoup(html_contents, 'html.parser')

    #- 3-2. 열 이름 추출
    tmp = soup.find_all('div', class_='inline-flex flex-nowrap justify-start items-end gap-0.5')
    eli_col_lst = []
    for col_name in tmp:
        col_name = str(col_name.text)
        col_name = col_name.replace('\n', '')
        col_name = col_name.strip()
        col_name = col_name.split('/')[0]
        col_name = col_name.strip()

        if col_name not in eli_col_lst:
            eli_col_lst.append(col_name)

    print(eli_col_lst) #-> 여기서 SOLO KILLS (단독처치) / FINAL BLOWS 데이터만 사용
    
    #- 3-3. 데이터 추출
    tmp = soup.find_all('td', class_='py-2 px-2 sm:first:px-4 sm:last:px-4')
    eli_data_lst = []
    pair_four = []
    for data in tmp:
        data = str(data.text)
        data = data.replace('\n', '')
        data = data.strip()
        
        pair_four.append(data)

        if len(pair_four) == 4:
            eli_data_lst.append(pair_four.copy())
            pair_four.clear()

    print(f'eli data 리스트: {eli_data_lst}') #- 내가 사용할 idx = 2, 3
    print(f'eli data length: {len(eli_data_lst)}')

    #- . pandas DataFrame 작성
    df = []

    for idx in range(len(hero_name_lst)):
        hero_name = hero_name_lst[idx]

        position = None
        if hero_name.upper() in tank_set:
            position = 'TANK'

        elif hero_name.upper() in dealer_set:
            position = 'DAMAGE'

        elif hero_name.upper() in healer_set:
            position = 'SUPPORT'

        else:
            print(f'[debug] - position 을 찾을 수 없음 / hero_name:{hero_name}')

        pick_rate = overview_lst[idx][0]
        win_rate = overview_lst[idx][1]
        kda = overview_lst[idx][2]

        damage_10min = str(primary_data_lst[idx][3])
        damage_10min = damage_10min.replace(',','')
        damage_10min = float(damage_10min)

        try:
            healing_10min = str(primary_data_lst[idx][4])
            healing_10min = healing_10min.replace(',','')
            healing_10min = float(healing_10min)
        except Exception as e:
            print(f'[error]: {e}')
            healing_10min = 0

        solo_kill_10min = eli_data_lst[idx][2]
        final_blows_10min = eli_data_lst[idx][3]

        df.append({'Hero':hero_name, 'Position':position, 'Pick Rate':pick_rate, 'Win Rate':win_rate, 'KDA':kda, 'Damage':damage_10min, 'Healing':healing_10min, 'Solo Kill':solo_kill_10min, 'Final Blows':final_blows_10min})

    print(df)

    df = pd.DataFrame(df)
    df.to_csv(f'Tableau/csv/ovbuff_{date}.csv', index=False, encoding='utf-8')