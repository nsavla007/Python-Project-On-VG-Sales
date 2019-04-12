#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:41:27 2018

@author: neelsavla
"""

import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("car.csv")
cols=['distance traveled','starting point']
df[cols].plot(kind='box',subplots=True)
plt.show()