import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression, LogisticRegression #- 선형 회귀 모델 / 로지스틱 회귀 모델
    #- 선형 = 연속적
    #- 로지스틱 = 범주(분류)
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, root_mean_squared_error
from sklearn.preprocessing import StandardScaler #- 스케일링

def p(title, data):
    return print(f'<{title}> \n {data} \n')

df = pd.read_csv('csv/customer_data.csv')

p('기본 df 정보 확인', df)

null_check = df.isnull().sum()
p('null 값 확인', null_check)

scaler = StandardScaler()
origin_data = df[['Age', 'AnnualIncome', 'On-Site_Time']]
scaled_data = scaler.fit_transform(origin_data)
df[['Age', 'AnnualIncome', 'On-Site_Time']] = scaled_data
p('스케일링화한 df', df)

# df['Gender'] = df['Gender'].replace('Male', 1)
# df['Gender'] = df['Gender'].replace('Female', 0)
df['Gender'] = df['Gender'].replace({'Male':1, 'Female':0}).astype(int)
p('Gender 값 변경', df)
p('Gender 타입 출력', df['Gender'].dtype)

all_data = train_test_split(df, train_size=0.8, test_size=0.2)
train_x = all_data[0][['Age', 'AnnualIncome', 'Gender', 'On-Site_Time']]
train_y = all_data[0][['SpendingScore']]
test_x = all_data[1][['Age', 'AnnualIncome', 'Gender', 'On-Site_Time']]
test_y = all_data[1][['SpendingScore']]

lin_model = LinearRegression()
lin_model.fit(X=train_x, y=train_y) #-> Score는 연속된 값
pred = lin_model.predict(X=test_x)
p('예측 결과', pred)
p('예측 정확도', root_mean_squared_error(y_true=test_y, y_pred=pred))

logis_model = LogisticRegression()
train_y = all_data[0]['Purchased'] #-> Yes / No 로 분류 가능
test_y = all_data[1]['Purchased']
logis_model.fit(X=train_x, y=train_y)
pred = logis_model.predict(X=test_x)
p('로지스틱(범주) 예측 결과', pred)
p('정확도 측정', accuracy_score(y_true=test_y, y_pred=pred))