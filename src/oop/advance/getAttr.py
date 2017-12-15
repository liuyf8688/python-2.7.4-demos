# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class Student(object):
    
    def __init__(self):
        
        self.name = 'liuyanfeng'
        
    def __getattr__(self, attr):
        
        if attr == 'score':
            
            return 99
        
student = Student()

print student.name
print student.score