#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:51:11 2018

@author: neelsavla
"""

import pandas as pd
df=pd.read_csv('pittsburgh2013.csv')
print(df['Max Dew PointF'].mean())
print(df['Max Humidity'].mean())
print(df['Max Dew PointF'].std())
print(df['Max Humidity'].std())