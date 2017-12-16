# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日

@author: tony
'''


import itertools, time

# 产生无限迭代器
'''
natuals = itertools.count(1)

for n in natuals:
    
    print n
    time.sleep(0.1)
'''

# 通过itertools.cycle('ABC')，产生一个无限循环这三个字符的迭代器

# 有限循环迭代器
ns = itertools.repeat('ABC', 10)

for n in ns:
    
    print n