# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))

s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

buffer = []
while True:
    
    d = s.recv(1024)
    if d:
        
        buffer.append(d)
    else:
        
        break;
    
data = ''.join(buffer)
s.close()

print data
