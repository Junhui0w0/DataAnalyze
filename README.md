# 데이터 분석
캡스톤디자인2 주제로 선정된 '유튜브 댓글 여론 분석' 을 원활하게 진행하기 위해 시작 \
Python을 활용해 댓글 추출할 예정이니, 데이터 분석도 Python-Pandas로 진행 \
데이터 분석 수업을 2번 정도 수강했지만, 처음부터 한다는 생각으로 기초부터 다지기

## 2025-03-15: Tutorial ##
1-1. Pandas에서는 주로 Series와 Dataframe을 주로 사용한다.

2-1. Series는 1차원 데이터로 구성되어 있다. \
2-2. 즉, 하나의 속성(N행 1열)으로 구성되어 있다. \
2-3. 행의 이름은 index=['a', 'b'...] 로 지정할 수 있다. \
2-4. List와 Dictionary를 통해 Series를 생성할 수 있다. \
2-5. 단, 문자+정수 와 같이 다른 데이터타입을 혼용해서 사용할 수 없다.

3-1. Dataframe(이하 DF)은 2차원 데이터(N행 M열)로 구성되어 있다. \
3-2. 속성의 이름은 Series와 마찬가지로 index를 통해 지정할 수 있다. \
3-3. Dictionary로 DF를 생성할 때, Key는 속성 이름을 Value는 해당 속성의 값을 나타낸다. \
3-4. df1.head() = 데이터 미리보기 \
3-5. df1.describe() = 각 속성 별 mean, std, min, max, sum 값 확인 \
3-6. df1[\'속성'].mena() = 각 속성의 평균 (mean은 std, min 등으로 변경 가능) \
3-7. df1.shape = df1의 행렬 크기 반환 \
3-8. df1.groupby('속성1')[\'속성2].mean() = 속성1과 속성2를 그룹으로 묶어 계산
3-8. pd.cut(df1[\'속성'], lst) = 각 속성에 있는 요소를 lst의 범위(?)에 따라 구분
3-8-1. lst=[\10,20,30,100] -> 속성값이 25 이면 (20,30) 을 반환함

----

## 2025-03-16: 인덱싱, 결측치, 그룹화 ##
1-1. 인덱싱하는 방법은 크게 loc와 iloc가 있다. \
1-2. loc는 Dataframe의 행 또는 열의 이름(라벨)을 사용한다. \
1-2-1. df.loc[[\'행1', '행2...'], [\'열1', '열2...']] = 지정 행과 열만 출력한다. \
1-3. iloc는 Dataframe의 index를 이용한다. (iloc의 i=index라고 생각하자) \
1-3-1. 즉, 이름이 아닌 인덱스(숫자)를 사용한다. \
1-3-2. df.iloc[[0:3], [1:7]] = 0\~2행 부터 1~6열을 출력한다. 

2-1. 결측치는 null 값을 대체하는 기능을 수행한다. \
2-2. 각 속성의 결측치 비율은 df.isnull().sum() / len(df) 를 통해 확인할 수 있다. \
2-3. df.fillna(대체값) 을 통해 null값을 변경할 수 있다. \
2-4. df[\'속성명'].fillna(df[\'속성명'].mean()) = 지정 속성의 null 값들을 평균값으로 대체한다. 

3-1. 그룹화는 df.groupby([\'속성1', '속성2'...])[\'속성3'] 으로 선언할 수 있다. \
3-1-1. 이는, 속성1과 속성2를 그룹으로 묶어 속성3 값을 확인할 수 있다. \
3-2. 그룹화변수.agg([\'min', 'max'...]) = 그룹화한 값의 최소, 최대... 값을 확인할 수 있다.

----

## 2025-03-19: 공공 데이터 활용 ##
이론적으로 개별적인 기능을 학습하는 것 보다 직접 데이터를 가지고 다루는 것이 효과적이라 판단 \
사용한 데이터셋: 월별 교통사고량(TAAS), 월별 어린이 교통사고량 (TAAS), 월별 강수량 (기상자료개방포털) \
자세한 링크는 Traffic_Accident/출처.txt 파일 참조 

----

## 2025-03-23: 데이터 전처리 및 플롯팅 ##
csv, excel 파일로부터 강수량과 사고량 추출 \
pyplot을 통해 3x3 크기의 플롯 생성 \
각 플롯에 년도별 사고량과 강수량 그래프 작성 

----

## 2025-03-26: 속도에 따른 어린이 사고 발생률 ##
속도에 따른 어린이(12살 미만)의 사건 발생률 조사 \
Nilsson의 Power Model 공식을 이용해 계산 \
