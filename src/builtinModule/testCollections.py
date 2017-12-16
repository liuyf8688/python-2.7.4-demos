# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日

@author: tony
'''

# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)

print p.x, p.y

print '======================================='

# deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')

print q

print '======================================='

# defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'


print dd['key1'], dd['key2']

print '======================================='

# OrderedDict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])

print d

od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])

print od

print '======================================='

# Counter
from collections import Counter

c = Counter()
for ch in 'programming':

    c[ch] = c[ch] + 1
    
print c
