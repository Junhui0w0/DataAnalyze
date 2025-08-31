import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

def p(title, data):
    return print(f'<{title}> \n {data} \n')

df = pd.read_csv('csv/penguins.csv')

null_check = df.isnull().sum()
p('결측치 값 확인', null_check)

#- 결측치 대체
df['sex'] = df['sex'].fillna('unknown') 

#- species 고유값 확인
unique_value = df['species'].unique()
p('species 고유값 확인', unique_value) #- ['Adelie' 'Gentoo' 'Chinstrap']

split_data = train_test_split(df, train_size=0.8, test_size=0.2)
train_df = split_data[0]
test_df = split_data[1]
p('train data', train_df)
p('test data', test_df)

model = LogisticRegression()
model.fit(X=train_df[['bill_length_mm', 'bill_depth_mm', 'body_mass_g']], y=train_df['species'])
res = model.predict(X=test_df[['bill_length_mm', 'bill_depth_mm', 'body_mass_g']])
p('에측 결과', res)
p('정확도', accuracy_score(y_true=test_df[['species']], y_pred=res))
# accuracy_score()

#==================================================================================#
#- LinearRegression vs LogisticRegression 
    #- LineaRegression은 model.fit을 수행할 때 y에 2차원 배열형태
    #- LogisticRegression은 model.fit을 수행할 때 y에 1차원 배열형태

#- 정확도 산출
    #1. 정수, 실수인 경우 -> mse
    #2. 그 외 -> accuracy_score