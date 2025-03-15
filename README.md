# DataAnalyze
캡스톤디자인2 주제로 선정된 '유튜브 댓글 여론 분석' 을 원활하게 진행하기 위해 시작 \
Python을 활용해 댓글 추출할 예정이니, 데이터 분석도 Python-Pandas로 진행 \
데이터 분석 수업을 2번 정도 수강했지만, 처음부터 한다는 생각으로 기초부터 다지기

## 2025-03-15: Tutorial ##
1-1. Pandas에서는 주로 Series와 Dataframe을 주로 사용한다.

2-1. Series는 1차원 데이터로 구성되어 있다. \
2-2. 즉, 하나의 속성(N행 1열)으로 구성되어 있다. \
2-3. 속성의 이름은 index=['a', 'b'...] 로 지정할 수 있다. \
2-4. List와 Dictionary를 통해 Series를 생성할 수 있다. \
2-5. 단, 문자+정수 와 같이 다른 데이터타입을 혼용해서 사용할 수 없다.

3-1. Dataframe(이하 DF)은 2차원 데이터(N행 M열)로 구성되어 있다. \
3-2. 속성의 이름은 Series와 마찬가지로 index를 통해 지정할 수 있다. \
3-3. Dictionary로 DF를 생성할 때, Key는 속성 이름을 Value는 해당 속성의 값을 나타낸다. \
3-4. df1.head() = 데이터 미리보기 \
3-5. df1.describe() = 각 속성 별 mean, std, min, max, sum 값 확인 \
3-6. df1[\'속성'].mena() = 각 속성의 평균 또는 총합을 구할 수 있다. (mean은 std, min 등으로 변경 가능) \
3-7. df1.shape = df1의 행렬 크기 반환 \
3-8. df1.groupby('속성1')[\'속성2].mean() = 속성1과 속성2를 그룹으로 묶어 계산
3-8. pd.cut(df1[\'속성'], lst) = 각 속성에 있는 요소를 lst의 범위(?)에 따라 구분
3-8-1. lst=[\10,20,30,100] -> 속성값이 25 이면 (20,30) 을 반환함