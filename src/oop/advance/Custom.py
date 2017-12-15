# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class Student(object):
    
    def __init__(self, name):
        
        self.name = name
        
    def __str__(self):
        
        return 'Student object (name: %s)' % self.name
    
    __repr__ = __str__
    
print Student('liuyanfeng')