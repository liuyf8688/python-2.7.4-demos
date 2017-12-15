# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(10, 20)