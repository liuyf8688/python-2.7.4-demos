# -*- coding: utf-8 -*-
'''
Created on 2017年12月18日

@author: tony
'''

from gevent import monkey; monkey.patch_all()
import gevent
import urllib2

def f(url):
    
    print 'GET: %s' % url
    resp = urllib2.urlopen(url)
    data = resp.read()
    print '%d bytes received from %s.' % (len(data), url)
    
gevent.joinall([
    
    gevent.spawn(f, 'https://www.python.org/'),
    gevent.spawn(f, 'https://www.yahoo.org/'),
    gevent.spawn(f, 'https://github.com/'),
])