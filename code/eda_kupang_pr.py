"""
eda_kupang_pr.py
Exploratory Data Analysis of BMKG Eltari dataset

Sandy H. S. Herho <herho@umd.edu>
2021/13/10
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

df = pd.read_csv('../data/laporan_iklim_harian.csv', usecols=['tanggal', 'pr'],
                parse_dates=True, dayfirst=True, index_col='tanggal')
df.replace(8888, np.nan, inplace=True)
print(df.isnull().values.any()) 
print(df.isnull().sum().sum()) 
print(df.shape[0])

dfNew = df.interpolate('pchip')
dfNew.to_csv('../data/dailyPrKupangInterp.csv', index=False)

plt.figure(figsize=(35, 10));
plt.plot(df['pr'], 'kx');
plt.plot(dfNew['pr']);
plt.xlabel('time', size=30);
plt.ylabel('precipitation (mm/day)', size=30);
plt.tight_layout();
plt.savefig('../figs/fig1.png');


mthPr = dfNew.resample('M').sum()
mthPr.to_csv('../data/monthlyPrKupang.csv')

fig, ax = plt.subplots(figsize=(20, 8))
mthPr.groupby(mthPr.index.month)["pr"].mean().plot(kind='bar', color='#0f82d4', 
                                                rot=0, ax=ax);
ax.set_xlabel('month', size=20);
ax.set_ylabel('precipitation (mm/month)', size=20);

labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']
ax.set_xticklabels(labels);
plt.savefig('../figs/fig3.png');

mthPr['year'] = mthPr.index.year
mthPr['month'] = mthPr.index.month
mthPr['precipitation'] = mthPr['pr']
mthPr = mthPr[['year', 'month', 'precipitation']]
mthPr.reset_index(drop=True, inplace=True)
mthPr.to_csv('../data/raiInput.csv', index=False)




