from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


data_link_lst = ['https://www.overbuff.com/heroes?platform=pc&timeWindow=month', 'https://www.overbuff.com/heroes?platform=pc&timeWindow=3months', 'https://www.overbuff.com/heroes?platform=pc&timeWindow=6months', 'https://www.overbuff.com/heroes?platform=pc&timeWindow=year']
    #- 데이터는 현재 시즌 ~ 4개의 이전 시즌정보만 제공함
    #- blizzard 공식 페이지에서는 아직 유저 데이터를 제공하는 데이터, api가 없어 팬페이지를 통해 데이터 수집

html_contents = None
with open('Tableau/owbuff_this_month.html', 'r', encoding='utf-8') as f:
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


#- 2. 영웅 이름(Hero) 추출
tmp = soup.find_all(class_='font-semibold uppercase whitespace-nowrap')
hero_name_lst = []
for hero_name in tmp:
    hero_name = hero_name.text
    hero_name = str(hero_name).replace('\n', '')
    hero_name = hero_name.strip()

    if hero_name not in hero_name_lst:
        hero_name_lst.append(hero_name)

print(len(hero_name_lst))

#- 3. 픽률(Pick Rate) / 승률(Win Rate) / 킬뎃(KDA) 추출
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

#- 4. pandas DataFrame 작성
df = []

for idx in range(len(hero_name_lst)):
    hero_name = hero_name_lst[idx]

    pick_rate = overview_lst[idx][0]
    win_rate = overview_lst[idx][1]
    kda = overview_lst[idx][2]

    df.append({'Hero':hero_name, 'Pick Rate':pick_rate, 'Win Rate':win_rate, 'KDA':kda})

print(df)

df = pd.DataFrame(df)
df.to_csv('ovbuff_overview.csv', index=False, encoding='utf-8')
print('CSV 데이터 생성 완료')