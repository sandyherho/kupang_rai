"""
rai_stl.py

RAI plot and STL decomposition
Sandy H. S. Herho <herho@umd.edu>
2021/10/24
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
plt.style.use('ggplot')
plt.rc("figure", figsize=(16, 12))
plt.rc("font", size=15)

df = pd.read_csv('../data/rai_kupang.csv')
rai = df['rai'].to_numpy()

fig = plt.figure(figsize=(15,8));
ax = fig.add_subplot(111);
xtime = np.linspace(1, rai.shape[0], rai.shape[0])
ax.plot(xtime, rai, 'black', alpha=1, linewidth=2);
ax.fill_between(xtime, 0., rai, rai > 0, color = '#54e1e3');
ax.fill_between(xtime, 0., rai, rai < 0, color = '#b81402');
plt.xlabel('time (month)', fontsize=15);
plt.ylabel('Rainfall Anomaly Index', fontsize=15);
ax.set_xlim(0, rai.shape[0]);
plt.tight_layout();
ax.set_xticklabels(['1978', '1986', '1994', '2003', '2011', '2019']);
plt.savefig('../figs/fig5.png');

rai = pd.Series(rai, index=pd.date_range("1-1-1978", periods=len(rai), freq="M"), name="RAI")

stl = STL(rai, seasonal=13)
res = stl.fit()
fig = res.plot()
plt.savefig('../figs/fig6.png')

