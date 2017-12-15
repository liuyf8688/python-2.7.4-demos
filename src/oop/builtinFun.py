# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class MyObject(object):
    
    def __init__(self):
        self.x = 9
        
    def power(self):
        return self.x * self.x
    
obj = MyObject()

print obj

print hasattr(obj, 'x')

print getattr(obj, 'x')

print '中国'
