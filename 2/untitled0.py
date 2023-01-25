# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:04:19 2023

df['job'].fillna(0, inplace=True)

@author: jksls
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as mpl

df = pd.read_csv('base\geoMap (4).csv')

df = df.dropna()
df = df.sort_values(by="job",ascending=False)
df = df.head(10)

x = np.array(df['Country'])
y = np.array(df['job'])

fig,ax = mpl.subplots(2,1)
ax[0].scatter(x,y)
tick_labels = ax[0].get_xticklabels()
tick_labels = [label.get_text()[:4] for label in ax[0].get_xticklabels()]
ax[0].set_xticklabels(tick_labels)

df = pd.read_csv('base\geoMap (5).csv')

df = df.dropna()
df = df.sort_values(by='university:',ascending=False)
df = df.head(10)

z = np.array(df['Country'])
v = np.array(df['university:'])

ax[1].scatter(z,v)
tick_labels = ax[1].get_xticklabels()
tick_labels = [label.get_text()[:4] for label in ax[1].get_xticklabels()]
ax[1].set_xticklabels(tick_labels)

mpl.show()