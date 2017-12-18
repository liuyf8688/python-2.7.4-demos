# -*- coding: utf-8 -*-
'''
Created on 2017年12月17日

@author: tony
'''

# 安装mysql驱动
# pip install mysql-connector==2.1.4 // 官方Python驱动

import mysql.connector

conn = mysql.connector.connect(user = 'root', password = '123456', database = 'world', use_unicode = True)

cursor = conn.cursor();
cursor.execute('select * from country')

values = cursor.fetchall()

cursor.close()
conn.close()

print values


