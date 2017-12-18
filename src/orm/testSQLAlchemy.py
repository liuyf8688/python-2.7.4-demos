# -*- coding: utf-8 -*-
'''
Created on 2017年12月17日

@author: tony
'''

# 安装ORM工具：pip install sqlalchemy

from sqlalchemy import Column, BigInteger, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    
    __tablename__ = 'User'
    
    id = Column(BigInteger, primary_key = True)
    user_name = Column(String(45))
    
engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/jiudingdb')
DBsession = sessionmaker(bind = engine)

session = DBsession()
# 插入数据
# new_user = User(id = 2, user_name = 'liumingyue')
# session.add(new_user)
# session.commit()

# 查询数据
user = session.query(User).filter(User.id == 2).one()
print 'type: ', type(user)
print 'name: ', user.user_name

session.close()

