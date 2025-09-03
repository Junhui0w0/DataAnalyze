import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Tableau/csv/ovbuff_month.csv')
scaler = StandardScaler()

# origin_PickRate = df[['Pick Rate']]
# scaled_pickrate = scaler.fit_transform(origin_PickRate)
# df['Scaled Pick Rate'] = scaled_pickrate

# origin_WinRate = df[['Win Rate']]
# scaled_winrate = scaler.fit_transform(origin_WinRate)
# df['Scaled Win Rate'] = scaled_winrate

origin_data = df[['Damage', 'KDA', 'Pick Rate', 'Win Rate', 'Solo Kill']]
scaled_data = scaler.fit_transform(origin_data)
df[['Scaled_Damage', 'Scaled_KDA', 'Scaled_Pick Rate', 'Scaled_Win Rate', 'Scaled_Solo Kill']] = scaled_data

scaled_df = pd.DataFrame(df)
scaled_df.to_csv('Tableau/csv/scaled_ovbuff_month.csv', index=False, encoding='utf-8')