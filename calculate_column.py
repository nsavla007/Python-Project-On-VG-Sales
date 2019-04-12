#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:05:50 2018

@author: neelsavla
"""

import pandas as pd
weather=pd.read_csv('pittsburgh2013.csv')
def to_celsius(F):
    return 5/9*(F-32)
df_celsius=weather[['Mean TemperatureF','Mean Dew PointF']].apply(to_celsius)
print((df_celsius).head())