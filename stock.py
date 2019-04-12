#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:27:06 2018

@author: neelsavla
"""

import pandas as pd 
import matplotlib.pyplot as plt
df1=pd.read_csv("stock.csv")
list2=['Jan', 'Feb']
df1[list2].plot()
plt.title('Stock Price')
plt.xlabel('')
plt.ylabel('Price in US Dollars')
plt.show()
