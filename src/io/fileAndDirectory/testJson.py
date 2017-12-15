# -*- coding: utf-8 -*-
'''
Created on 2017年12月13日

@author: tony
'''

import json

d = dict(name = 'liuyanfeng', age = 20, score = 88)

print json.dumps(d)

print '=============================='

jsonStr = '{"age": 20, "score": 88, "name": "liuyanfeng"}'

print json.loads(jsonStr)

print '=============================='

class Student(object):
    
    def __init__(self, name, age, score):
        
        self.name = name
        self.age = age
        self.score = score
        
student = Student('liuyanfeng', 20, 88)

print json.dumps(student, default = lambda obj: obj.__dict__);