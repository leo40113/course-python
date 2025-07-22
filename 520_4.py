# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:57:33 2022

@author: leo40
"""

def calc(w, *args):
    for arg in args:
        w = w * arg
    return w

def calc2(w, **kwargs):
    print(w, kwargs)
y = calc(4, 7, 5, 8)
print(y)
calc2('哈哈', c=7, e=5, f=8)