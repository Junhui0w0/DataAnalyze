import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')

def p(title, data):
    return print(f'<{title}> \n {data} \n')

df= pd.read_csv('csv/advertising.csv')

#1. 데이터 불러오기
p('기본 df 정보', df)

#2. 데이터 시각화 - tv 광고비 & sales 산점도 표현
plt.scatter(data=df, x='TV', y='sales')
plt.show()

#3. 선형회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X=df[['TV']], y=df[['sales']]) 
    #X=독립변수 / y=종속변수
    #독립변수 = 내가 추후에 predict에 넣을 입력값
    #종속변수 = 입력값으로 인해 도출될 결과값

    #기본적으로 scikit learn은 여러 개의 데이터를 동시에 처리할 수 있게 되어있음
    #이로 인해 하나의 데이터를 사용할 때에도 2차원 배열 형태로 만들어야 함. (df[['sales']])

test_data = pd.DataFrame({'TV':[100]})
res = model.predict(test_data)
print('TV 광고비가 100일 때의 예상 판매량', res)


#=========================================================#

df = pd.read_csv('csv/advertising.csv')
data = train_test_split(df, train_size=0.8, test_size=0.2)
p('train 데이터', data[0])
p('test 데아터', data[1])

#data[0] = train
x = data[0][['TV', 'radio']]
y = data[0][['sales']]

model1 = LinearRegression()
model1.fit(X=x, y=y)

print(f'학습된 모델의 계수: {model1.coef_} / 절편: {model1.intercept_}')

test_x = data[1][['TV', 'radio']]
res = model1.predict(X=test_x)
print(f'판매량 예측 결과 \n {res}')

#- from sklearn.model_selection import train_test_split
#- from sklearn.linear_model imort LinearRegression
    #model.fit(X=train_x, y=train_y)
        #X = input값 / y=출력값 -> 두 값 모두 2차원 배열 형태로 줘야 함
    #model.predict(X=test_x)
        #입력값을 통해 출력값 예측

#================================================================#

from sklearn.metrics import mean_squared_error #mse = 평균 제곱 오차 = 실제값과 예측값의 차이를 제곱한 것 -> 0에 가까울 수록 모델 성능 좋음
test_y = data[1][['sales']]

diff = mean_squared_error(y_true=test_y, y_pred=res)
p('예측값과 실제값의 MSE', diff)