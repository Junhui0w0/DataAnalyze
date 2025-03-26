import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import calendar

#어린이 교통사고
age_under_12_TA_df_list = [[] for i in range(7)]
print(age_under_12_TA_df_list)
tmp = pd.read_excel(
    'Traffic_Accident/어린이교통사고_2016_2020.xls',
    header=None
)

print(tmp) #[0][2]~[65][2]
idx = 0

for i in range(1,66):
    print(f'index={i}, tmp[i][1]={tmp[i][1]}, tmp[i][2]={tmp[i][2]}')
    if i % 13 == 1:
        print(tmp[i][1])
        continue

    age_under_12_TA_df_list[idx].append(int(tmp[i][2]))

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

    age_under_12_TA_df_list[idx].append(int(tmp[i][2]))

    if i % 13 == 0:
        idx += 1

print(age_under_12_TA_df_list)