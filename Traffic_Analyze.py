import pandas as pd
import seaborn as sns

# 강수량-csv / 월별교통사고 xlsx / 어린이교통사고 xls
rain_df = pd.read_csv(
    'Traffic_Accident/2016_2022_강수량.csv',
    header=None,
    skiprows=8,
    nrows=84,
    encoding='cp949',
    usecols=[0, 1, 2]
)
print(rain_df) #csv는 encoding 명시

#TA = Traffic Accident
monthly_TA_df_list = []
for i in range(2016, 2023):
    file_name = f'Traffic_Accident/{str(i)}년 월별 교통사고.xlsx'
    monthly_TA_df_list.append(pd.read_excel( #excel은 encoding 명시 안해도되는듯? 알아서 감지하고 바꾸는듯
        file_name,
        header=None
    ))
print(monthly_TA_df_list,'\n')

#pip install xlrd
age_under_12_TA_df_list = []
tmp = pd.read_excel(
    'Traffic_Accident/어린이교통사고_2016_2020.xls',
    header=None
)
print(f'[어린이 교통사고] \n {tmp}')

