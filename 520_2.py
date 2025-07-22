# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:12:59 2022

@author: leo40
"""
s = [(3, 4), (2, 4), (5, 3)]
def bbb(w, h):
    return w*h

def callbbb(conta, func):
    for r in conta:
        print(func(r[0],r[1]), end=' ')

callbbb(s, bbb)
