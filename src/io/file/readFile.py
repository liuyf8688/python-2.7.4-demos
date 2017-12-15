# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

try:
    
    f = open('../../../resources/io/example.txt', 'r')

    print f.read()

finally:

    if f:
        
        f.close()
        
print "================================"
        
# using with ... as ...
with open('../../../resources/io/example.txt', 'r') as f:
    
    print f.read()
    

print "================================"
        
with open('../../../resources/io/example.txt', 'r') as f:
    
    for line in f.readlines():
        
        print line.strip()