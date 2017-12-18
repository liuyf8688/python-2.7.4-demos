# -*- coding: utf-8 -*-
'''
Created on 2017年12月17日

@author: tony
'''

from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print 'Serving HTTP on port 8000 ...'

httpd.serve_forever()