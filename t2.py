#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:19:23 2018

@author: neelsavla
"""

import pandas as pd 

df1=pd.read_csv("temp.csv")
list1=['vapPress']
df1[list1].plot()
list2=['tempDiff', 'BtempDiff']
df1[list2].plot()