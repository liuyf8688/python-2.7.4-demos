# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日

@author: tony
'''

# 将32位无符号数变成字节
n = 10240099
b1 = chr((n & 0xff000000) >> 24)
b2 = chr((n & 0xff0000) >> 16)
b3 = chr((n & 0xff00) >> 8)
b4 = chr(n & 0xff)

s = b1 + b2 + b3 + b4

print s

print '==================================='

# 通过struct模块来解决str和其它二进制数据类型的转换
import struct

print struct.pack('>I', 10240099)