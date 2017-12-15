# -*- coding: utf-8 -*-
'''
Created on 2017年12月14日

@author: tony
'''

import time, threading

def loop(interval):
    
    print 'thread %s is running ...' % threading.current_thread().name
    
    n = 0
    while n < 5:
        
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(interval)
        
    print 'thread %s ended.' % threading.current_thread().name
    
print 'thread %s is running ...' % threading.current_thread().name
t1 = threading.Thread(target = loop, args = (2, ))
# 可以指定线程名
t2 = threading.Thread(target = loop, args = (1, ),  name = 'LoopThread-t2')

t1.start()
t2.start()

t1.join()
t2.join()

print 'thread %s ended.' % threading.current_thread().name