# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日

@author: tony
'''

import re

if re.match(r'^\d{3}\-\d{3,8}$', '010-12345678'):
    
    print 'ok'

else:
    
    print 'failed'
    
print re.split(r'\s+','a b    c')
