# -*- coding: utf-8 -*-
'''
Created on 2017年12月13日

@author: tony
'''
'''
import platform
print platform.python_version()
'''

from multiprocessing import Process
import os

def run_proc(name):
    
    print 'Run child process %s (%s)...' % (name, os.getpid())
    
if __name__ == '__main__':

    print 'Parent process %s.' % os.getpid()
    p = Process(target = run_proc, args = ('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'