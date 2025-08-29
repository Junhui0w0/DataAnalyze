import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')

df = pd.read_csv('csv/online_sales.csv')

#1. 데이터 전처리
print('<df info>')
df.info()

def p(title, data):
    return print(f'<{title}> \n {data} \n')

is_null = df.isnull().sum()
p('결측치 확인', is_null)

df['수량'] = df['수량'].fillna(1)
p('결측치 채우기', df)

df['주문일자'] = pd.to_datetime(df['주문일자'])
p('주문일자 데이터 타입 변경', df['주문일자'].dtypes)

# df['상품명'] = df['상품명'].drop_duplicates()
# df['고객ID'] = df['고객ID'].drop_duplicates()
df = df.drop_duplicates(subset=('고객ID', '상품명'))
p('상품명 & 고객ID 중복 행 제거', df)

col_total = df['수량'] * df['가격']
print(col_total)

df['총 판매 금액'] = col_total
p('총 판매 금액 열 추가', df)

#2. 데이터 시각화
#2-1. 카테고리 별로 총 판매 금액을 보여주는 막대그래프를 그려라
    #막대그래프 = 카테고리 별 수치 파악

category_total = df.groupby('카테고리')['총 판매 금액'].sum().reset_index()
sns.barplot(data= category_total, x='카테고리', y='총 판매 금액')
plt.show()

#2-2. 가장 많은 판매량을 기록한 상품 5개를 막대 그래프로 출력해라
product_lst = df['상품명']
cnt_lst = df['수량']

res_lst = []
for i in range(len(product_lst)):
    res_lst.append((cnt_lst.iloc[i], product_lst.iloc[i]))

res_lst.sort(reverse=True) #cnt(수량)을 0번 index에 넣었고, reverse=True 이니 내림차순 정렬

sorted_product_lst = []
sorted_cnt_lst= []
for cnt, product in res_lst:
    sorted_product_lst.append(product)
    sorted_cnt_lst.append(cnt)

ranking_5_df= pd.DataFrame()
ranking_5_df['수량'] = sorted_cnt_lst[:5]
ranking_5_df['상품명'] = sorted_product_lst[:5]

sns.barplot(data=ranking_5_df, x='상품명', y='수량')
plt.show()


top_5 = df.groupby('상품명')['수량'].sum().nlargest(5).reset_index()
sns.barplot(data=top_5, x='상품명', y='수량')
plt.show()

#2-3. 일자별 총 판매 금액의 추이를 보여주는 선 그래프 -> plot?
date_total = df.groupby('주문일자')['총 판매 금액'].sum().reset_index()
plt.plot(date_total['주문일자'], date_total['총 판매 금액'])
plt.show()

#3. 인사이트
    #1. 전자기기의 총 판매금액이 가장 높다
    #2. 가장 많이 팔린 상품은 티셔츠-키보드-블루투스 이어폰-커피머그컵-청바지 순 이다.
    #3. 가장 많은 수익을 낸 날은 2024-01-02이다.


#============================================================================#
#- plt 선 그래프
    # plt.plot(x, y)

#- plt 산점도
    # plt.scatter(x='col1', y='col2', data=df)
        # 파라미터 c = color (색상 지정 가능)
        # 파라미터 s = size (점 크기 지정 가능)

#- seaborn 산점도
    # sns.scatterplot(x='col1', y='col2', data=df)

#- seaborn histplot
    # sns.histplot(x='col1', data=df)
    # 데이터 분포 비교에 주로 사용

#- seaborn barplot
    # sns.barplot(x='col1', y='col2', data=df)
    # 카테고리 별 값 비교에 주로 사용

#- 여러 중복 행 제거
    # df = df.drop_duplicates(subset=('col1', 'col2', ...))

#- 그룹별 데이터 분석
    # df_group = df.groupby('col1')['col2'].sum().reset_index()
        # col1 -> col1을 기준으로 여러 값들을 묶겠다.
        # col2 -> col1을 기준으로 묶었을 때 col2의 값에 대한 이후 함수(sum, mean 등)를 계산한다.
        # reset_index() -> groupby 와 하나의 세트라고 생각하면 편함 
            # groupby 이후 index가 col 이름으로 변경되는 문제 해결해줌

#- 최대 N개의 데이터만 출력
    # df_group = df.groupby('col1')['col2'].mean().nlargest(N).reset_index()
        # col1을 기준으로 데이터를 묶고, col2의 값에 대한 평균을 큰 것부터 N개만 추출
        # 작은 것부터 추출 -> nsmallest(N)
        
