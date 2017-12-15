# -*- coding: utf-8 -*-
'''
Created on 2017年12月11日

@author: tony
'''


' a test module '

__author__ = 'Tony Liu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'
        
if __name__ == '__main__':
    test()
    
