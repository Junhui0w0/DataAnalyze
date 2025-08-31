import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font="Malgun Gothic", 
        rc={"axes.unicode_minus":False},
        style='darkgrid')

def p(title, data):
    return print(f'<{title}> \n {data} \n')

df = pd.read_csv('csv/movie_reviews.csv')

print('<df 기본 정보>')
df.info()

#- 결측치 확인
null_check = df.isnull().sum()
p('각 행 별 결측치 확인', null_check)
 
#- '리뷰내용' 의 결측치 -> '내용 없음' / '평점' 결측치 -> 영화 평균 평점
df['리뷰내용'] = df['리뷰내용'].fillna('내용 없음')

rate_avg = df['평점'].mean()
rate_avg = round(rate_avg, 1)
df['평점'] = df['평점'].fillna(rate_avg)
p('결측치 채우기', df)

null_check = df.isnull().sum()
p('각 행 별 결측치 확인', null_check)

#- '작성일' -> datetime 타입 변환
df['작성일'] = pd.to_datetime(df['작성일'])
p('작성일 타입 변환', df['작성일'].dtype)

#- 모든 열의 값이 동일한 행 제거
check_same_row = df.duplicated()
p('동일 행 확인', check_same_row)

df = df.drop_duplicates()
p('동일 행 제거', df)

#- '영화제목' & '리뷰내용' 동일한 중복 리뷰 제거
del_title_rev = df.drop_duplicates(subset=('영화제목', '리뷰내용'))
p('영화제목, 리뷰내용 동일 중복 행 제거', del_title_rev)

#- 평점의 분포를 보여주는 히스토그램(sns.histplot) 출력
sns.histplot(data=df, x=df['평점'])
plt.title('평점 분포')
plt.show()

#- 영화제목별로 평균 평점을 비교하는 막대그래프 출력
    #1. 영화제목별로 그룹묶기 -> groupby('영화제목')
    #2. 평균 평점 비교 -> ['평점'].mean().reset_index()
groupby_title = df.groupby('영화제목')['평점'].mean().reset_index()
sns.barplot(data=groupby_title, x='영화제목', y='평점')
plt.title('영화제목 별 평균 평점')
plt.show()

#- 날짜별 작성된 리뷰 수 추이 선 그래프 출력
    #1. 날짜별 그룹 묶기 -> df.groupby('날짜')['리뷰내용'].count().reset_index()
groupby_date = df.groupby('작성일')['리뷰내용'].count().reset_index()
plt.plot(groupby_date['작성일'], groupby_date['리뷰내용'])
plt.title('날짜별 작성된 리뷰 수')
plt.show()

#- 인사이트
    #1. 평점의 분포는 9.5가 가장 높다. 이는 모든 영화가 대체로 좋은 평을 받았음을 알 수 있다.
    #2. 영화제목별로 평점을 구분한 결과, 가장 낮은 평점이 7점대를 가장 높은 평점이 9점대를 기록한 것으로 보아 그리 큰 차이가 없다. 즉, 모든 영화의 평이 좋다고 볼 수 있다.
    #3. 0517에 가장 많은 리뷰수가 달린 것으로 보아, 해당 날에 신규 출시된 영화가 가장 많았음을 유추해 볼 수 있다.