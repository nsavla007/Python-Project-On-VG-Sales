#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:12:54 2018

@author: neelsavla
"""

import matplotlib.pyplot as plt
life_exp=[30,40,50,60,70,80,90]

gdp_cap=[0,10000,20000,30000,40000,50000,60000]

plt.plot(gdp_cap, life_exp)

plt.show()

plt.xlabel(' GDP per CApita in USD')
plt.ylabel('Life Expectancy')
plt.title('World Development')

plt.plot(gdp_cap, life_exp)
#plt.show()

tick_val=[10000,20000,30000,40000,50000,60000]
tick_lab=['10K','20k','30K','40K','50K','60K']
plt.xticks(tick_val,tick_lab)
plt.show()