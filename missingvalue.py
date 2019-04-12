#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:51:22 2018

@author: neelsavla
"""

import pandas as pd
titanic=pd.read_csv('titanic.csv')
df=titanic[['age','cabin']]
#print(df)
# drop rows in the data frame for any NA values
#print(df.dropna(how='any'))
#.shape attribute helps to see the effect of dropping the missing values from the data frame.
print(df.dropna(how='any').shape)
#drop columns in titanic with less than 1000 non missing values.
#print(titanic.dropna(thresh=1000,axis='columns').info())