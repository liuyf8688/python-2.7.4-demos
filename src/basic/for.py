# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

lists = { 1, 2, 3, 4, 5}

for item in lists:
    print item
    
print '===================================='

for i, item in enumerate(lists):
    print i, item
    
print '===================================='

print range(1, 11)

print '===================================='

print [x * x for x in range(1, 11)]