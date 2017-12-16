# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

from PIL import Image, ImageFilter

im = Image.open('test.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
