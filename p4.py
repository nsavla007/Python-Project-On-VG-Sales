#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:57:32 2018

@author: neelsavla
"""
import pandas as pd
country_names=['United States','Australia','Japan','India']
driving_direction=[True,False,False,False]
veh=[891,725,650,321]
country_dict={'country':country_names,'driving':driving_direction,'veh_per_thousand':veh}
data_frame_1 =pd.DataFrame(country_dict)
#print(data_frame_1)
row_lables=['US','AUS','JAP','IND']
data_frame_1.index=row_lables
print(data_frame_1)
