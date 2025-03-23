import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

# 강수량-csv / 월별교통사고 xlsx / 어린이교통사고 xls
rain_df = pd.read_csv(
    'Traffic_Accident/2016_2022_강수량.csv',
    header=None,
    skiprows=8,
    nrows=84,
    encoding='cp949',
    usecols=[0, 1, 2]
)
# print(rain_df) #csv는 encoding 명시


# lst = []
# lst.append(rain_df[:][2][1])
# print(type(lst[0]))


rain_lst = [[0]*12 for i in range(7)] #2016 ~ 2022 / 12월
idx = 0
for i in range(7):
    for j in range(12):
        rain_lst[i][j] = int(rain_df[:][2][idx]) #슬라이싱으로 하면 시간 단축 될듯?
        idx += 1

# print(rain_lst) #년도 별 강수량 추출



#TA = Traffic Accident
TA_lst = [[0]*12 for i in range(7)]
for i in range(2016, 2023):

    file_name = f'Traffic_Accident/{str(i)}년 월별 교통사고.xlsx'
    TA_df = pd.read_excel( #excel은 encoding 명시 안해도되는듯? 알아서 감지하고 바꾸는듯
        file_name,
        header=None
    )

    for idx in range(12):
        print(f'{i}-{idx+1}월 사고 발생률: {TA_df[1:][1][idx+1]}')
        # print(f'type: {type(TA_df[1:][1][idx+1])}') #str
        TA_lst[i-2016][idx] = int((TA_df[1:][1][idx+1]).replace(',',''))

# print(TA_lst) #년도 별 사고량 추출


# plot 작성
years = list(range(2016, 2023)) #2016 ~ 2022
months = list(calendar.month_abbr)[1:]  # ['Jan', 'Feb', ..., 'Dec']

# 3x3 서브플롯 생성
fig, axes = plt.subplots(3, 3, figsize=(20, 15)) #3x3 // 전체는 20inch x 15inch
fig.suptitle('월 별 강수량과 교통사고 연관 관계 (2016-2022)', fontsize=18, y=0.95)

# 각 연도별 플롯 생성
for idx, year in enumerate(years):
    row = idx // 3
    col = idx % 3
    ax = axes[row][col]
    
    # 강수량 데이터 플롯 (파란색)
    ax.plot(months, rain_lst[idx], 
            marker='o', 
            # color='#1f77b4',
            color = 'blue',
            linewidth=2,
            label='Rainfall')
    
    # 사고율 데이터 플롯 (주황색)
    ax2 = ax.twinx()
    ax2.plot(months, TA_lst[idx], 
             marker='s', 
            #  color='#ff7f0e',
             color='orange',
             linestyle='--', 
             linewidth=2,
             label='Accidents')
    
    # 축 및 레이블 설정
    ax.set_title(f'{year}', fontsize=14, pad=15)
    ax.set_ylabel('Rainfall (mm)', color='#1f77b4', fontsize=10)
    ax2.set_ylabel('Traffic Accidents', color='#ff7f0e', fontsize=10)
    
    # 그리드 및 범례
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))
    ax2.legend(loc='upper right', bbox_to_anchor=(0.98, 0.98))

# 빈 서브플롯 숨기기
for i in range(len(years), 9):
    row = i // 3
    col = i % 3
    axes[row][col].axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.92, hspace=0.4, wspace=0.3)
plt.show()





# #pip install xlrd
# #어린이 교통사고
# age_under_12_TA_df_list = [0,1]
# tmp = pd.read_excel(
#     'Traffic_Accident/어린이교통사고_2016_2020.xls',
#     header=None
# )
# age_under_12_TA_df_list[0] = tmp

# tmp = pd.read_excel(
#     'Traffic_Accident/어린이교통사고_2021_2022.xls',
#     header=None
# )
# age_under_12_TA_df_list[1] = tmp


# # 강수량(rain_df)에 비례한 사고 발생률(TA)


# # 속도에 비례한 사고 발생률