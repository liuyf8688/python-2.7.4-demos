# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

import types

class Animal(object):
    def run(self):
        print 'Animal is running ...'
        
class Dog(Animal):
    def run(self):
        print 'Dog is running ...'
    
    def eat(self):
        print 'Eating meat ...'

class Cat(Animal):
    pass

'''
dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
'''

print type(123)
print type('liuyanfeng')
print type(None)

print type(abs)
print type(Cat)
print type(Cat())

print type('liuyanfeng') == types.StringType

animal = Animal()
dog = Dog()

print isinstance(dog, Dog)

print dir('ABC')
print len('ABC')
print 'ABC'.__len__()

class MyObject(object):
    def __len__(self):
        return 100
    
print len(MyObject())

print 'ABC'.lower()