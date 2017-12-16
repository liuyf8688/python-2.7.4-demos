# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

from PIL import Image

im = Image.open('test.jpg')
w, h = im.size

im.thumbnail((w // 2, h // 2))

im.save('test2.jpg', 'jpeg')