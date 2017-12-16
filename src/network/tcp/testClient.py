# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

import socket, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

print s.recv(1024)
for data in ['liuyanfeng', 'liumingyue']:
    
    s.send(data)
    print s.recv(1024)
    
time.sleep(60 * 60)
s.send('exit')
s.close()