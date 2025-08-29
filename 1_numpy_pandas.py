import pandas as pd
import numpy as np

lst = [10,20,30,40,50]
lst2 = [[100,200,300],[400,500,600]]
lst3 = [100,200,300,400,500]

arr = np.array(lst)
print(arr.shape) #-> m열

arr2 = np.array(lst2)
print(arr2.shape) #2차원 -> n행 m열

#==============================================#

arr = np.array(lst)
arr2 = np.array(lst3)
print(f'덧셈: {arr + arr2}')
print(f'곱셈: {arr * 10}')

#==============================================#

data = {'name': ['a', 'a2', 'a3'],
    'age':[10, 20, 30],
    'city':['seoul', 'japan', 'us']      
} #-> 입력은 dict
    #dict의 key -> df의 열
    #dict의 value -> df의 value

df = pd.DataFrame(data)
print(df, '\n')

#==============================================#

print(f'<나이 열만 출력> \n {df["age"]} \n') #나이 열만 출력
print(f'<나이가 20 이상인 사람 정보만 출력> \n {df[df["age"] >= 20]} \n') #나이가 20 이상인 사람의 정보만 선택

#==============================================#

score_data = pd.read_csv('csv/score.csv')
print(f'<score.csv 데이터> \n {score_data} \n') #- 전체 데이터 출력
print(f'<수학 점수가 90점 이상인 사람> \n {score_data[score_data["수학"] >= 90]} \n') #-수학 점수가 90점 이상

def p(title, data):
    return print(f'<{title}> \n {data} \n')

people_num = len(score_data['이름'])

korean_avg = sum(score_data['국어']) / people_num
p('국어 성적의 평균', korean_avg)

math_avg = sum(score_data['수학']) / people_num
p('수학 성적의 평균', math_avg)

eng_avg = sum(score_data['영어']) / people_num
p('영어 성적의 평균', eng_avg)


pd_eng_avg = score_data['영어'].mean()
p('영어 성적의 평균 - pd', pd_eng_avg)

pd_people_num = score_data['이름'].count()
p('사람 수', pd_people_num)

#==================================#
#- 기본 arr 생성
    #arr = np.array(lst명)

#- 기본 df 생성
    #data = {'col':[...]} -> 딕셔너리 형태
    #df = pd.DataFrame(data)

#- csv 파일 읽어오기
    #csv_data = pd.read_csv('csv파일명')
    
#- pandas 내장 함수
    #1. 평균 -> df['colname'].mean()
    #2. 갯수 -> df['colname'].count()
    #3. 합계 -> df['colname'].sum()
#==================================#