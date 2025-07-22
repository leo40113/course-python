# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:37:04 2022

@author: user
"""

def add(aaa):
    x=1
    for a in range(1, aaa):
        x=x*a
    return x
    
x=add(10)
print(x)
