# -*- coding: utf-8 -*-
"""
Created on Fri May 20 19:03:21 2022

@author: leo40
"""

def aaa(name, title='未知'):
    print(f'name={name}, title={title}')
    
aaa('安安','你好')

def bbb(w, h):
    return [((w+h)*2, w*h),'正方形' if w==h else '長方形']

a, b = bbb(4, 7)
print(a, b)