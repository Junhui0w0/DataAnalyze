import pandas as pd

# Series 생성(w.List) - 임의 데이터 생성
ages = pd.Series([10,20,30], name='Age_Series', index=['A', 'B', 'C']) #-> index=행 이름
print(f'Age(List-Series)\n {ages}\n')


# Series 생성 (w.Dict) - 임의 데이터 생성
sal_dict = {'A': 1000, 'B':3000, 'C':'2천만원'}
sal_Series = pd.Series(sal_dict)
print(f'Salary(Dict-Series)\n {sal_Series}\n')
#-> 단 하나의 속성을 가지며, 단일 데이터 타입만 가능(정수, 문자열 혼합 X)
#-> 속성 이름은 지정할 수 없음 // 행 이름은 index로 지정


# DataFrame 생성 - 임의 데이터 생성
data = {'Name': ['Alice', 'Bob'], 'Age':[25,30]} #-> #Key:Value (Key=속성 이름, Value=해당 속성의 값)
df = pd.DataFrame(data, index=['ID1', 'ID2']) #-> index=행 이름
print(f'Data(dict-Dataframe)\n {df}\n')


# DataFrame 생성 - CSV 파일 읽기
df = pd.read_csv('Titanic-Dataset.csv') 
print('df(read_csv) Titatic\n', df)

print(f'\ndf.head()\n{df.head()}') # 첫번째 속성을 기준으로 5개 정도 출력 (미리보기 용도인듯()
print(f'\ndf.describe()\n{df.describe()}') #각 속성 별 Count(Null이 아닌 값 갯수), mean(평균), std(표준편차), min, max 등..
print(f'\ndf.shape()\n {df.shape}') #차원 확인 (행,열)

sur_rate = df['Survived'].mean() #평균 생존률
age_dist = df['Age'].value_counts() #연령별 분포
sex_sur_rate = df.groupby('Sex')['Survived'].mean() #성별 간 생존률
Pclass_sur_rate = df.groupby('Pclass')['Survived'].mean() #Pclass 별 생존률

print('\n평균 생존률\n', sur_rate)
print('\n연령별 분포도\n', age_dist)
print('\n성별 간 생존률\n', sex_sur_rate)
print('\nPclass 간 생존률\n', Pclass_sur_rate)

bins = [0,18,30,50,100]
df['AgeGroup'] = pd.cut(df['Age'], bins) #Age라는 속성에 있는 각 요소를 bins 범위에 맞춰 출력
print(f'pd.cut["Age"], bins 이후 \n {df.head()}')


#=====================================================================#
# 1-1. Series는 1차원 데이터
# 1-2. index를 통해 행 이름 지정 가능
# 1-3. 열 이름은 별도로 지정 불가능?
# 1-4. List와 Dictionary로 Series 생성 가능

# 2-1. Dataframe은 2차원 데이터
# 2-2. index = 행 이름 지정
# 2-3. head() = 데이터 미리보기
# 2-4. describe() = 각 속성 별 평균, 표편, 최소, 최대 값 확인
# 2-5. shape = 행, 열 크기 파악 가능
# 2-6. df['속성'].mean() -> 해당 속성의 평균값 (mean은 max, std 등으로 변경 가능)
# 2-7. df.groupby('속성1')['속성2'].mean() = 두 속성을 그룹으로 묶어 분석(mean은 max, std 등으로 변경 가능)
# 2-8. pd.cut(df['속성'], lst) = 속성의 각 요소를 lst 범위에 따라 컷
#=====================================================================#