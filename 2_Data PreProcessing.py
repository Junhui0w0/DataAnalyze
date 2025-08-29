import numpy as np
import pandas as pd

def p(title, data):
    return print(f'<{title}> \n {data} \n')

#1. 결측치 처리
df = pd.read_csv('csv/sales_data_dirty.csv')
p('전체적인 데이터 프레임', df)

is_null = df.isnull() #- 각 value에 대해서 NaN(null)값인 경우 True로 반환
p('결측치 확인 - True/False', is_null)

is_null_count = df.isnull().sum() #- 각 열에 대해서 결측치의 갯수 출력
p('결측치 갯수 확인', is_null_count) #- '판매량' 부분에서 결측치 하나 관찰됨

is_null_lst = []
df_col = df.columns
p('df.columns의 타입', type(df_col))

for i in range(len(df_col)):
    if is_null_count.iloc[i] != 0: #- 결측치 갯수가 0이 아닌 경우 -> 결측치가 있다
        col_name = df_col[i]
        is_null_lst.append(col_name) #- 결측치 발생 col 기록

p('결측치 발생 column', is_null_lst)

#1-1. 결측치 제거
df_drop_null = df.dropna()
p('결측치 제거', df_drop_null)

df_drop_null_null_count = df_drop_null.isnull().sum()
p('결측치 제거 확인', df_drop_null_null_count)

#1-2. 결측치 대체 - 해당 행의 평균으로
for null_col in is_null_lst:
    print(f'[debug] - 결측치 발생 col: {null_col}')

    avg_value = round(df[null_col].mean(), 1)
    p('avg value', avg_value)

    replace_df = df[null_col].fillna(avg_value)
    p('replace null', replace_df)

    df[null_col] = replace_df
    p('replace df', df)

#2. 데이터 타입 변환
for i in range(len(df_col)):
    col_name = df_col[i] #column 이름

    unique_value = df[col_name].unique()
    print(f'unique_value = {unique_value}')

replace_df = df['가격'].replace('알 수 없음', np.nan) #-replace(old, new) -> old값을 new로 변경
p('replace ', replace_df)
print(f'replace_df type: {type(replace_df)}') #- type=object 이기에 mean 불가

replace_df = replace_df.astype(float) # type=float로 변환
p('astype -> float', replace_df)

avg_value = round(replace_df.mean(), 1)
print(f'avg_value : {avg_value}')

df['가격'] = replace_df
df['가격'] = df['가격'].fillna(avg_value)
p('df의 알 수 없음 변경',df)

p('df의 날짜 컬럼 데이터타입', type(df['날짜'])) #- <class 'pandas.core.series.Series'>
    #Pandas의 datetime 형식으로 변경 -> to_datetime()

df['날짜'] = pd.to_datetime(df['날짜'])
p('df의 날짜 컬럼 데이터타입', df['날짜'].dtypes)

#================================================#
#- 결측치 검출
    # df.isnull() -> 각 value에 대해 결측치(NaN)이면 True / 그렇지 않으면 False
    # df.isnull().sum() -> 각 열에 대해 결측치의 갯수 출력

#- 결측치 제거
    # df.dropna() -> 결측치가 포함된 행 제거

#- 결측치 채우기
    # df.fillna(value) -> 결측치가 있는 곳에 새로운 값 삽입

#- 특정 값 대체
    # df.replace(old_value, new_value) -> 이전 값을 새로운 값으로 변경 가능
        #NaN이 아닌 다른 쓸모없는 값(ex: '알 수 없음') 등을 변경

#- 타입 변경
    # df.astype(타입명) -> str, float, int 등
    # df.astype({'col_name': 타입명}) -> 특정 컬럼의 타입 변경 (변경할 수 없는 경우 에러 발생)
        #에러 제어: https://www.geeksforgeeks.org/python/python-pandas-dataframe-astype/

#- 시계열 데이터 변환
    # df = pd.to_datetime(df['시계열 데이터로 변경할 컬럼명'])