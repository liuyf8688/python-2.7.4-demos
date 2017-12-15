# -*- coding: utf-8 -*-
'''
Created on 2017年12月14日

@author: tony
'''

import threading

local_school = threading.local()

def process_student():
    
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)
    
def process_thread(name):
    
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target = process_thread, args = ('liuyanfeng', ), name = 'Threading-A')
t2 = threading.Thread(target = process_thread, args = ('liumingyue', ), name = 'Threading-B')

t1.start()
t2.start()

t1.join()
t2.join()