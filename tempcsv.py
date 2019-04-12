#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:11:19 2018

@author: neelsavla
"""

import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("temp.csv")
df.plot(color='red')
plt.title('Temperature Data')
plt.xlabel('')
plt.ylabel('Index')
plt.show()