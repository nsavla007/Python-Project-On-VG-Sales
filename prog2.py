#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:25:51 2018

@author: neelsavla
"""

europe={'spain':'madrid','france':'paris','germany':'berlin','norway':'oslo' }
#print(europe)
#print(europe['france'])
#print(europe.keys())
europe['italy']='rome'
#print(europe)
#print('italy' in europe)
europe['Austria']='vienna'
#print(europe)
del(europe['Austria'])
print(europe)