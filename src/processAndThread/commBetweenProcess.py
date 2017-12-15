# -*- coding: utf-8 -*-
'''
Created on 2017年12月14日

@author: tony
'''

from multiprocessing import Process, Queue
import os, time, random

def write(q):
    
    for value in ['A', 'B', 'C']:
        
        print 'Put %s to queue ...' % value
        q.put(value)
        time.sleep(random.random())

def read(q):
    
    while True:
        
        value = q.get(True)
        print 'Get %s from queue.' % value
        
if __name__ == '__main__':
    
    # 父进程创建Queue, 并传给各个子进程
    q = Queue();
    pw = Process(target = write, args = (q, ))
    pr = Process(target = read, args = (q, ))
    
    pw.start()
    pr.start()
    
    pw.join()
    pr.terminate()