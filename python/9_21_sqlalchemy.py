#!user/bin/env python3
# -*- coding:utf-8 -*-

"""sql"""

__author__ = 'Guowei'

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建User
Base = declarative_base()
class User(Base):
    __tablename__ = 'user'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))

def test_sqlalchemy():
    # 初始化数据库连接
    engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/test')
    DBSession = sessionmaker(bind=engine)
    # 创建session 对象
    session = DBSession()
    # new_user = User(id='2',name = 'Bob')
    # session.add(new_user)
    user = session.query(User).filter(User.id =='2').one()
    print(user.name)
    session.commit()
    session.close()

if __name__ == '__main__':
    test_sqlalchemy()