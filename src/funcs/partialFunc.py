# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

import functools

print int('123456')

print int('123456', base = 8)

print int('64', 16)

print '=================================='

int2 = functools.partial(int, base = 2)
print int2('1000000')