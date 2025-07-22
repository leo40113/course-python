# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:40:41 2022

@author: leo40
"""

def add(aaa):
    x=0
    for a in z:
        x=x+a
    return x

def mul(aaa):
    x=1
    for a in z:
        x=x*a
    return x
    
def callall(value, func):
    return func(value)

z = [1, 2, 4]
funcs = [add, mul]
for f in funcs:
    print(callall(z, f))