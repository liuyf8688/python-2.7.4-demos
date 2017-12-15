# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''
def add(x, y, f):
    return f(x) + f(y)

print add(-5, 6, abs)