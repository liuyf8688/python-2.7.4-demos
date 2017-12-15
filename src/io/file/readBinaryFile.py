# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

with open('../../../resources/io/gbk.txt', 'rb') as f:
    
    print f.read().decode('gbk')
    
print '==============================='

import codecs

with codecs.open('../../../resources/io/gbk.txt', 'r', 'gbk') as f:
    
    print f.read()