#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:52:18 2018

@author: neelsavla
"""

import pandas as pd
games=pd.read_csv('vgsales.csv')
del games['Rank_2000']
games.drop_duplicates(subset="Name",keep= 'first' ,inplace= True)
print(games.dropna())
