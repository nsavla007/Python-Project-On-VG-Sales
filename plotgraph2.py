#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:10:41 2018

@author: neelsavla
"""
import matplotlib.pyplot as plt
lst_life_exp=[30,40,50,60,70,80,90]
lst_gdp=[0,1000,2000,3000,4000,5000,6000]
#plt.plot(lst_gdp,lst_life_exp)
#plt.scatter(lst_gdp,lst_life_exp)
#plt.xscale('log')  #logarithmic scales
lst_grade=[50,60,70,80,80,90,100,75,70,65,90,80]
plt.hist(lst_grade, bins=10)
#plt.show()
plt.clf()
life_exp_1995=[20,30,40,50,60,70,80]
plt.hist(life_exp_1995, bins=15)
plt.show()