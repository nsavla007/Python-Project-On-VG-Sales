#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:40:27 2018

@author: neelsavla
"""

europe={'spain':{'capital':'madrid','population':45.3},
        'france':{'capital':'paris','population':66.2},
        'germany':{'capital':'berlin','population':32}}
#print(europe)
#print(europe['france']['capital'])
europe['italy']={'capital':'rome','population':21.5}
#print(europe)
#print(europe['italy']['population'])
data={'capital':'rome','population':21.5}
europe['italy']=data
print(europe)