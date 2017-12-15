# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class Student(object):
    
    __slots__ = ('name', 'age')
    

student = Student()

student.name = 'liuyanfeng'
student.age = 34

student.score = 99