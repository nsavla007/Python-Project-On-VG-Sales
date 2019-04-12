#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:34:53 2018

@author: neelsavla
"""

import pandas as pd
df1=pd.read_csv("file_messy.csv", delimiter=' ',header=None)
#print(df1)
print(df1.head())
df1.to_csv('file_clean.csv')
df1.to_excel('file_clean1.xls', index=False)


