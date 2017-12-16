# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['liuyanfeng', 'liumingyue']:
    
    s.sendto(data, ('127.0.0.1', 9999))
    print s.recv(1024)
    
s.close()