# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

import os

print os.name

print '==================================='

# Window下没有该函数
#print os.uname()

print os.environ

print '==================================='

print os.getenv('PATH')

print '==================================='

print os.path.abspath('.')

print '==================================='

print os.path.join('.', 'test')

print '==================================='

os.rmdir(os.path.join('.', 'test'))

os.mkdir(os.path.join('.', 'test'))

print os.path.split('/a/b/c/abc.txt')

print '==================================='

print os.path.splitext('/a/b/c/abc.txt')

print '==================================='

# 过滤目录

print [x for x in os.listdir('.') if os.path.isdir(x)]
