#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:10:14 2018

@author: neelsavla
"""

import pandas as pd
import matplotlib.pyplot as plt
titanic=pd.read_csv('titanic.csv')
fig, axes=plt.subplots(nrows=3,ncols=1)
titanic.loc[titanic['pclass']==1].plot(ax=axes[0],y='fare',kind='box')
titanic.loc[titanic['pclass']==2].plot(ax=axes[1],y='fare',kind='box')
titanic.loc[titanic['pclass']==3].plot(ax=axes[2],y='fare',kind='box')
