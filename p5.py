#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 11:15:39 2018

@author: neelsavla
"""

import pandas as pd
cars=pd.read_csv('cars.csv')
#print(cars[0:4])
#print(cars[3:6])
#print(cars[['Origin','Model']])  # we use 2 square brackets to use data frame
print(cars[['MPG','Cylinders']])