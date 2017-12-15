# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''
def f(x):
    return x * x

print map(f, [1, 2, 3, 4, 5])

'''
 examples of reduce
'''
def add(x, y):
    return x + y

print reduce(add, [1, 2, 3, 4, 5])

def fn(x, y):
    return x * 10 + y

print reduce(fn, [1, 2, 3, 4, 5])