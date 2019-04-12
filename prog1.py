#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 10:21:52 2018

@author: neelsavla
"""
import pandas as pd
names=['United States','Australia', 'Japan','India','Russia']
driving_direction=[True,False,False,False,True]
cars_per_pop=[809,730,580,19,201]
dict={'country':names,'driving_direction':driving_direction,'cars_per_pop':cars_per_pop}
cars_df=pd.DataFrame(dict)
#print(cars_df)

rows_labels=['US','AUS','JAP','IN','RU']
cars_df.index=rows_labels
#print(cars_df[['country']])

#print(cars_df[['country','driving_direction']])

#print(cars_df[0:3])

#print(cars_df[3:6])

#print(cars_df.iloc[2])  #gives all details of position 2

#print(cars_df.loc[['AUS','IN']])    # calls with labels not index.

#print(cars_df.iloc[4,0],cars_df.iloc[4,1])

#print(cars_df.loc[['IN','RU'],['country','driving_direction']])

#print(cars_df.loc[:,['cars_per_pop','driving_direction']])

#print(cars_df.iloc[:,[1]])
