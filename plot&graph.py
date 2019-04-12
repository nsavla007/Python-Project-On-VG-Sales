#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:03:51 2018

@author: neelsavla
"""
import matplotlib.pyplot as plt
lst_pop=[]
for i in range(5):
    lst_pop.append(i)
lst_year=[2000,2001,2002,2003,2004]
print(lst_year)
plt.plot(lst_year,lst_pop)
plt.show()
