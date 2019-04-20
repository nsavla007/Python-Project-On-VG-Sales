#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:41:49 2018

@author: neelsavla
"""

import pandas as pd
df=pd.read_csv('titanic.csv')
print(df['fare'].describe()) #describe is the key word which helps to get summary of the data.
df['fare'].plot(kind='box')
