import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x=[1,2,3,4]
y=[2,4,6,8]

# plt.plot(x,y) #= 선 
# plt.show()

# plt.scatter(x,y) #- 점
# plt.show()

# plt.plot(x,y) #- 선 그래프
# plt.title('data analyze')
# plt.xlabel('x-label')
# plt.ylabel('y-label')
# plt.show()

# df = pd.DataFrame({'x':[1,2,3,4,5], 'y':[10,7,23,12,17]})
# sns.scatterplot(x='x', y='y', data=df) #- seaborn의 산점도
# plt.show()

# sns.histplot(x='x', data=df) #- 히스토그램: 데이터 분포 확인 - 빈도수 시각화
# plt.show()

# sns.barplot(x='x', y='y', data=df) #- 카테고리 별로 수치 데이터 비교
# plt.show()

#==========================================#

iris_df = pd.read_csv('csv/iris.csv')

def p(title, data):
    return print(f'<{title}> \n {data} \n')

# iris_df.info()

p('iris df 전체 정보', iris_df)

plt.scatter(x='sepal_length', y='sepal_width', data=iris_df)
plt.show()

# sns.histplot(x='petal_length', data=iris_df)
# plt.show()

#1. matplotlib의 산점도(sepal_length, sepla_width) / 종에 따라 색깔을 다르게 표시, 점의 크기는 petal_length에 비례하게 설정
species_lst = list(iris_df['species'].unique())
color_lst = []

for i in range(len(iris_df['species'])):
    species = iris_df['species'].iloc[i]
    idx = species_lst.index(species)

    color_lst.append(idx * 100)

plt.scatter(x='sepal_length', y='sepal_width', data=iris_df, c=color_lst, s='petal_length') #- c=color / s=size
plt.show()

sns.scatterplot(data=iris_df, x='sepal_length', y='sepal_width', hue='species', sizes='petal_length') #- hue=색조 (주어진 파라미터를 기준으로 색상을 unique한 갯수로 구분)
plt.show()

#2-1. species 별로 petal_length의 평균을 비교하는 막대 그래프를 그려라
petal_length_avg = []

for name in species_lst:
    avg = iris_df['petal_length'][iris_df['species'] == name].mean()
    petal_length_avg.append((name, avg))

print(petal_length_avg)

sns.barplot(x='species', y='petal_length', data=iris_df) #- 카테고리 별 수치 비교 -> 자동으로 평균값 산정해서 출력함
plt.show()

#2-2. species 별로 petal_length의 분포를 보여주는 바이올린 플롯을 그려라
sns.violinplot(data=iris_df, x='species', y='petal_length')
plt.show()

