# -*- coding: utf-8 -*-
'''
Created on 2017年12月17日

@author: tony
'''

def application(environ, start_response):
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')

