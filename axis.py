#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:31:41 2018

@author: neelsavla
"""

import matplotlib.pyplot as plt
lst_life_exp=[30,40,50,60,70,80,90]
lst_gdp=[0,1000,2000,3000,4000,5000,6000]
plt.plot(lst_gdp,lst_life_exp)
xlab='GDP per Capita [in USD]'
ylab='Life Expectancy [in years]'
title='World Development'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.show()