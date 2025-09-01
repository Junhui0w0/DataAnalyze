import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def p(title, data):
    return print(f'<{title}> \n {data} \n')

df = pd.read_csv('csv/superstore_sales.csv')

print('<df.info> \n')
df.info()

p('df.describe()', df.describe())

#1. 동일 행 제거
df = df.drop_duplicates()
p('동일 행 제거', df)

#2. 시계열 데이터 변환 (Order Date)
df['Order Date'] = pd.to_datetime(df['Order Date'])
p('Order Date 시계열 데이터 타입으로 변환', df['Order Date'].dtype)

#3. Total Sales 열 추가
total_sales = df['Sales'] * df['Quantity']
df['Total Sales'] = total_sales
p('Total Sales 열 추가', df)

#4. 결측치 확인 및 처리
check_null = df.isnull().sum()
p('결측치 확인', check_null)

#5. sns - 막대그래프 - Category별로 Profit 시각화
groupby_category_profit = df.groupby('Category')['Profit'].mean().reset_index()
sns.barplot(data = groupby_category_profit, x='Category', y='Profit')
plt.show()

#6. plt - 선그래프 - 연도별 Total Sales 추세 시각화
date_lst = df['Order Date']
year_lst =[]

for i in range(len(date_lst)):
    date = date_lst[i]
    print(f'debug - year: {str(date)[:4]}')

    year = str(date)[:4]
    year_lst.append(year)

df['Year'] = year_lst
p('year 열 추가', df)

groupby_year_totalSales = df.groupby('Year')['Total Sales'].mean().reset_index()
plt.plot(groupby_year_totalSales['Year'], groupby_year_totalSales['Total Sales'])
plt.show()

#7. Seaborn - 막대그래프 - 수익성 Top5 Sub-Category
groupby_subCategory_profit = df.groupby('Sub-Category')['Profit'].sum().nlargest(5).reset_index()
sns.barplot(data=groupby_subCategory_profit, x='Sub-Category', y='Profit')
plt.show()

#8. 인사이트
    #1. 카테고리 별로 수익화의 평균을 나타낸 결과, 모든 카테고리들이 음수를 나타내고 있다.(이는, 사업화에 있어서 큰 타격이며 가장 큰 적자를 보고 있는 부분은 Technology이다.)
    #2. 연도별 총 판매금액을 나타낸 결과, 2015년에 가장 큰 판매실적을 올렸으며 2014년과 2016년은 서로 비슷한 양상을 보이고 있다.
    #3. 서브 카테고리를 기준으로 분류한 결과 의자-책장-가구-라벨-미술품 순으로 수익이 높은 것을 확인할 수 있다.