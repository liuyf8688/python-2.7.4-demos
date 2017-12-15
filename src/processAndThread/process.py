# -*- coding: utf-8 -*-
'''
Created on 2017年12月13日

@author: tony
'''

# 该文件只有在xUnix下可运行

'''
import os

print 'Process (%s) start ...' % os.getpid()

pid = os.fork()

if pid == 0:

    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
else:

    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)

'''