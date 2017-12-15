# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

import functools

def log(text):
    
    def decorator(func):
        
        @functools.wraps(func)
        def wrapper(*args, **kw):
            
            print '%s %s():' % (text, func.__name__)
            
            return func(*args, **kw)
        
        return wrapper
    
    return decorator

@log('execute')
def now():
    print '2017-12-12'
    
nowObj = log('execute')(now)

print nowObj.__name__