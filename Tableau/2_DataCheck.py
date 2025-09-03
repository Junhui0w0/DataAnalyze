import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def p(title, data):
    return print(f'\n <{title}> \n {data} \n')

name_lst = ['month', '3months', '6months', 'year']

for name in name_lst:

    df = pd.read_csv(f'Tableau/csv/ovbuff_{name}.csv')

    # p('기본 DF 정보', df)

    check_null = df.isnull().sum()
    p('결측치 확인', check_null)

    # print('각 col별 데이터타입 확인')
    # df.info()

    # col_damage = df['Damage']
    # p('damage col 확인', col_damage)

    # col_heal = df['Healing']
    # p('healing col 확인', col_heal)