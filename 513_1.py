# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:40:42 2022

@author: user
"""

while True:
    s = input('請輸入100的除數:')
    try:
        i = 100 / float(s)
        print('100 除', s, '=', i)
        break
    except ValueError as e:
        print('發生 ValueError 例外:', e)
    except ZeroDivisionError:
        print('發生 ZeroDivisionError 例外:')
    except:
        print('其他例外')
    print('進入下個迴圈')
print('正常結束')
