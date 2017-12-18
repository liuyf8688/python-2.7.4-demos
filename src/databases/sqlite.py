# -*- coding: utf-8 -*-
'''
Created on 2017年12月16日

@author: tony
'''

import os, sqlite3

# 删除数据库文件
os.remove(os.path.join('.', 'test.db'))

conn = sqlite3.connect('test.db')

cursor = conn.cursor()
cursor.execute('create table user (id int primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (1, \"liuyanfeng\")')
print cursor.rowcount

cursor.execute('insert into user (id, name) values (2, \"liumingyue\")')
print cursor.rowcount

cursor.execute('select * from user')
values = cursor.fetchall()

print values

cursor.close()
conn.commit()
conn.close()