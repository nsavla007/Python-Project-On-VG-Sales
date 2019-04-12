#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:13:20 2018

@author: neelsavla
"""

import pandas as pd
import matplotlib.pyplot as plt
games=pd.read_csv('vgsales1.csv')
count=pd.value_counts(games['Genre'].values)
print(count)
fig=count.plot(kind='bar')
fig.set_title('Top Genres')
fig.set_xlabel('Name of Genre')
fig.set_ylabel('Count of Genre')
plt.show()