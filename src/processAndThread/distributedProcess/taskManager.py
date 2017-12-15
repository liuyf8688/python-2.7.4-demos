# -*- coding: utf-8 -*-
'''
Created on 2017年12月14日

@author: tony
'''

import random, multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = multiprocessing.Queue()
result_queue = multiprocessing.Queue()

# 为解决__main__.<lambda> not found问题
def get_task_queue():
    
    return task_queue

# 为解决__main__.<lambda> not found问题
def get_result_queue():
    
    return result_queue

class QueueManager(BaseManager):
    
    pass

# 添加freeze_support，否则会报错
if __name__ == '__main__':
    
    freeze_support()

    QueueManager.register('get_task_queue', callable = get_task_queue);
    QueueManager.register('get_result_queue', callable = get_result_queue);
    
    manager = QueueManager(address = ('127.0.0.1', 5000), authkey = '123456')
    manager.start()
    
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    
    for i in range(10):
        
        n = random.randint(0, 1000)
        print 'Put task %d ...' % n
        task.put(n)
        
    print 'Try get results ...'
    
    for i in range(10):
        
        r = result.get(timeout = 10)
        print 'Result: %s' % r
        
    manager.shutdown()