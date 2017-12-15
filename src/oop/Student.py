# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class Student(object):
    
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
        
    def print_score(self):
        print '%s %s' % (self.__name, self.__score)
        
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
        
foo = Student('liuyanfeng', 100)
# print foo.__name
print foo.get_name()
foo.print_score()
foo.age = 34
print foo.age
print foo.get_grade()

bar = Student('liumingyue', 50)
print bar.age
print bar

print Student