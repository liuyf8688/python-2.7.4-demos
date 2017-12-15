# -*- coding: utf-8 -*-
'''
Created on 2017年12月13日

@author: tony
'''

try:
    
    import cPickle as pickle
    
except ImportError:
    
    import pickle
    
d = dict(name = 'liuyanfeng', age = 20, score = 99)

print pickle.dumps(d)

# 从文件中读取序列化后的内容

'''
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close
print d
'''

print '==========================================='
