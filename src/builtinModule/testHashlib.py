# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日

@author: tony
'''

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')

print md5.hexdigest()

print '============================================'

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?')

print sha1.hexdigest()