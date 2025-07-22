# -*- coding: utf-8 -*-
"""
Created on Fri May 27 18:47:28 2022

@author: leo40
"""

# def prnprice1(name, c1, c2, c3):
#　    print(f'{name},', c1, c2, c3)
    
def prnprice(name, **kwargs):
    print(f'{name},', kwargs)

prnprice('chris', red=3, green=7, blue=7)

dict4 = {'red': 3, 'green': 7, 'blue': 7}
prnprice('chris', **dict4)
prnprice('chris', dict4)

# print(prnprice1)