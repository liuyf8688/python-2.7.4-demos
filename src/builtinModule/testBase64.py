# -*- coding: utf-8 -*-
'''
Created on 2017年12月15日

@author: tony
'''

import base64

print base64.b64encode('binary\x00string')

print base64.b64decode('YmluYXJ5AHN0cmluZw==')

# url safe base 64
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')
