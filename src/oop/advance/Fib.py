# -*- coding: utf-8 -*-
'''
Created on 2017年12月12日

@author: tony
'''

class Fib(object):
    
    def __init__(self):
        
        self.a, self.b = 0, 1
        
    def __iter__(self):
        
        return self
    
    def next(self):
        
        self.a, self.b = self.b + self.a, self.a + self.b
        
        if (self.a > 100000):
            
            raise StopIteration()
        
        return self.a
    
    def __getitem__(self, n):
        
        
        if isinstance(n, int):
            a, b = 1, 1
        
            for x in range(n):
            
                a, b = b, a + b
            
            return a
    
        if isinstance(n, slice):
        
            start = n.start
            stop = n.stop
            
            a, b = 1, 1
            L = []
            for x in range(stop):
                
                if (x >= start):
                    
                    L.append(a)
                    
                a, b = b, a + b
                
            return L
        

    
for n in Fib():

    print n
    
    
print "======================================"

f = Fib()

print f[0]
print f[1]
print f[2]
print f[3]

print "======================================"

fib = Fib()
print f[0:100]