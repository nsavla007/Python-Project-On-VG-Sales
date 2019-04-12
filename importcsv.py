#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:27:57 2018

@author: neelsavla
"""

import pandas as pd
df1=pd.read_csv("world_population.csv")
print(df1)

new_labels=['Year of Population','World Population']
df2=pd.read_csv("world_population.csv",header=0,names=new_labels)
print(df2)

