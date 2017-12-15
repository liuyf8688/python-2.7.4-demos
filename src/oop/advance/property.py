# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class Student(object):
    
    @property
    def score(self):
        
        return self._score
    
    @score.setter
    def score(self, value):
        
        if not isinstance(value, int):
            
            raise ValueError('score must be an integer!')
        
        if value < 0 or value > 100:
            
            raise ValueError('score must between 0 ~ 100!')
        
        self._score = value
        
        
student = Student()

student.score = 60

print student.score

student.score = 1000

print student.score
