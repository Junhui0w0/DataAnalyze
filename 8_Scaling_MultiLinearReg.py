import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

def p(title, data):
    return print(f'<{title}> \n {data} \n')

df = pd.read_csv('csv/superstore_sales.csv')
p('DF 구조', df)

scaler = StandardScaler()
    #- fit 주어진 데이터를 평균0, 표준편차1로 재구성
    #- transform 재구성한 평균과 표준편차를 적용

x = df[['Sales', 'Quantity']]
scaled_x = scaler.fit_transform(x)
scaled_df = pd.DataFrame(scaled_x, columns=['Sales', 'Quantity'])
p('스케일링화된 DF', scaled_df)

scaler1 = StandardScaler()
sales = df[['Sales']]
scaled_sales = scaler1.fit_transform(sales)
df['Sales'] = scaled_sales
p('sales 열 스케일링', df)

scaler2 = StandardScaler()
quantity = df[['Quantity']]
scaled_quantity = scaler2.fit_transform(quantity)
df['Quantity'] = scaled_quantity
p('Quantity - 스케일링화', df)

from sklearn.model_selection import train_test_split
data = train_test_split(df, train_size=0.8, test_size=0.2)
train_df = data[0]
test_df = data[1]

x = train_df[['Sales', 'Quantity']]
y = train_df[['Profit']]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error
lin_model = LinearRegression()
lin_model.fit(X=x, y=y) #- Linear회귀 모델은 y가 2차원 데이터
res = lin_model.predict(X=test_df[['Sales', 'Quantity']])
p('예측값', res)
p('예측값과 실제값 차이', root_mean_squared_error(y_true=test_df[['Profit']], y_pred=res))

#===================================================#
#- train_test_split
    # data = train_test_split(df, train_size=percent, test_size=percent) -> train x,y / test x,y 로 크게 4가지로 분할 후 진행 권장
    # train_x = data[0][['col1', 'col2']]
    # train_y = data[0][['col3']]
    # test_x = data[1][['col1', 'col2']]
    # test_y = data[1][['col3']]

    # model.fit(x=train_x, y=train_y)
    # res = model.predict(x=test_x)
    # diff = mean_squarred_error(y_true=y_test, y_pred=res)