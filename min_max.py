#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:33:41 2018

@author: neelsavla
"""

import pandas as pd
df=pd.read_csv('percent-bachelors-degrees-women-usa.csv')
print(df['Engineering'].min())
print(df['Engineering'].max())
mean=df.mean(axis='columns')
mean.plot()