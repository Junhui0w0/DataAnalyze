import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv') 
print(f'df.describe()\n {df.describe()}\n')
print(f'df.head()\n {df.head()}\n')
print(f'df\n {df}\n')

# 인덱싱 - loc (행, 열 라벨(이름) 이용)
print(df.loc[0, 'Name'],'\n') #df.loc[행 이름, 열 이름]
print(df.loc[[0,1], ['Name', 'Sex']],'\n') #0,1 행의 Name과 Sex만 추출

mask = (df['Age'] >=60) & (df['Sex'] == 'male') #60세 이상 & 남성
print(f'df.loc[mask]: \n {df.loc[mask]}\n')

# 인덱싱 - iloc (위치 기반, index 사용)
df_iloc1 = df.iloc[0:3, 1:6] #0~2행 , 1~5열 -> 어떤 열을 추출했는지 파악 힘듬
print(f'df.iloc[0:3, 1:6] \n {df_iloc1} \n')

df_iloc2 = df.iloc[::2, :] #행: 전체 행렬 단, 2씩 증가(짝수) / 열: 모든 열
print(f'df.iloc[::2, :] \n {df_iloc2} \n')

# 인덱싱 - 볼리언 (상위 N%)
top_10 = df['Fare'] > df['Fare'].quantile(0.9) #90% 초과한 Fare Value만 추출
print(f'top 10 of Fare \n {df[top_10]} \n')


# 결측치 처리 - 탐지 및 분석
import seaborn as sns
import matplotlib.pyplot as plt

# # 시각화
# sns.heatmap(df.isnull()) # cabin(1등) -> age -> embarked 순으로 결측치 많음
# plt.show()

null_rate = df.isnull().sum() / len(df) * 100
print(f'결측치 비율\n {null_rate} \n')

# 결측치 대체 (중앙값)
df_fillna_0 = df.fillna(0)
print(f'결측치 0 대체 \n {df_fillna_0} \n')

df_fillna_mean = df['Age'].fillna(df['Age'].mean())
print(f'결측치 평균값 대체 \n {df_fillna_mean} \n')


# 그룹 분석
group = df.groupby(['Pclass', 'Sex'])['Fare'] # 클래스+성별 별 비용 분석(-> 1등급 남성 / 1등급 여성 / 2등급 남성...)
res = group.agg(['min', 'mean', 'max'])
print(res)
# -> 남성은 아예 안내거나, 여성 최고가와 근접 또는 동일