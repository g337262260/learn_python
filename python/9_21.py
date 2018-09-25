#!user/bin/env python3
# -*- coding:utf-8 -*-

"""sql"""

__author__ = 'Guowei'


import os, sqlite3
import mysql.connector
def findMysql():
    # 导入MySQL驱动:
    # 注意把password设为你的root口令:
    conn = mysql.connector.connect(user='root', password='123456', database='test')
    cursor = conn.cursor()
    # 创建user表:
    cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    # 插入一行记录，注意MySQL的占位符是%s:
    cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    cursor.rowcount
    # 提交事务:
    conn.commit()
    cursor.close()
    # 运行查询:
    cursor = conn.cursor()
    cursor.execute('select * from user where id = %s', ('1',))
    values = cursor.fetchall()
    print(values)
    # 关闭Cursor和Connection:
    cursor.close()
    conn.close()




def addData():
    db_file = os.path.join(os.path.dirname(__file__), 'test.db')
    if os.path.isfile(db_file):
        os.remove(db_file)

    # 初始数据:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
    cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
    cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
    cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
    cursor.close()
    conn.commit()
    conn.close()


def get_score_in(low, high):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from user where score>= ? and score <=?',(low,high))
    # cursor.execute('select * from user order by score desc')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    print(values)


if __name__ =='__main__':
    findMysql()


