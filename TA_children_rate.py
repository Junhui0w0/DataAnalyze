import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

speed_before = int(input("속도 변화 전 속도: "))
speed_after = int(input("속도 변화 후 속도: "))
n = int(input("경미한 부상(2) / 중상 사고(3) / 치명적 사고(4): "))
TA_rate_related_speed = (speed_after / speed_before) ** n

children_TA_list = [[] for i in range(7)]
print(children_TA_list)

tmp = pd.read_excel(
    'Traffic_Accident/어린이교통사고_2016_2020.xls',
    header=None
)

print(tmp[65]) #[0][2]~[65][2]
idx = 0

for i in range(1,66):
    print(f'index={i}, tmp[i][1]={tmp[i][1]}, tmp[i][2]={tmp[i][2]}')
    if i % 13 == 1:
        print(tmp[i][1])
        continue

    children_TA_list[idx].append(int(tmp[i][2]))

    if i % 13 == 0:
        idx += 1
        


tmp = pd.read_excel(
    'Traffic_Accident/어린이교통사고_2021_2022.xls',
    header=None
)

for i in range(1,27):
    print(f'index={i}, tmp[i][1]={tmp[i][1]}')

    if i % 13 == 1:
        print(tmp[i][1])
        continue

    children_TA_list[idx].append(int(tmp[i][2]))

    if i % 13 == 0:
        idx += 1

print(children_TA_list)


children_TA_list2 = [[0]*12 for i in range(7)]

# Nilsson의 Power Model - 속도에 따른 사고 발생률
for i in range(7):
    for j in range(12):
        children_TA_list2[i][j] = children_TA_list[i][j] * (1-TA_rate_related_speed)

speed_lst = [i for i in range(30, 150, 10)]
TA_rate = []    



# plot 작성
years = list(range(2016, 2023)) #2016 ~ 2022
months = list(calendar.month_abbr)[1:]  # ['Jan', 'Feb', ..., 'Dec']

# 3x3 서브플롯 생성
fig, axes = plt.subplots(3, 3, figsize=(20, 15)) #3x3 // 전체는 20inch x 15inch
fig.suptitle('Monthly Accident Related With Children', fontsize=18, y=0.95)

# 각 연도별 플롯 생성
for idx, year in enumerate(years): #2016 ~ 2022 (7개년)
    row = idx // 3 #0 ~ 2
    col = idx % 3 # 0 ~ 2 (3x3 크기)
    ax = axes[row][col]
    
    # 어린이 교통사교율 (주황색)
    ax.plot(months, children_TA_list[idx], 
            marker='o', 
            color='orange',
            linewidth=2,
            label='Children TA')
    
    ax.plot(months, children_TA_list2[idx], 
            marker='o', 
            color='red',
            linewidth=2,
            label='Children TA (changing speed)')
    

    # 축 및 레이블 설정
    ax.set_title(f'{year}', fontsize=14, pad=15)
    ax.set_xlabel('Month', fontsize=12)
    ax.set_ylabel('Number', fontsize=12)
    
    # 그리드 및 범례
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', bbox_to_anchor=(0.02, 0.98))

# 빈 서브플롯 숨기기
for i in range(len(years), 9):
    row = i // 3
    col = i % 3
    axes[row][col].axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.92, hspace=0.4, wspace=0.3)
plt.show()