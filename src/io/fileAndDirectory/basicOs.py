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

# 创建空文件
def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)
        

def touch2(fname, times=None):
    fhandle = open(fname, 'a')
    try:
        os.utime(fname, times)
    finally:
        fhandle.close()

touch('test.txt')
# 删除文件是os.remove(path)
#os.remove(os.path.join('.', 'test.txt'))

os.rmdir(os.path.join('.', 'test'))

os.mkdir(os.path.join('.', 'test'))

print os.path.split('/a/b/c/abc.txt')

print '==================================='

print os.path.splitext('/a/b/c/abc.txt')

print '==================================='

# 过滤目录

print [x for x in os.listdir('.') if os.path.isdir(x)]
