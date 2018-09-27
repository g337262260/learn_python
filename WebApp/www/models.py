#!user/bin/env python3
# -*- coding:utf-8 -*-

"""model"""
import asyncio

import orm

__author__ = 'Guowei'

import time, uuid
from orm import Model, StringField, BooleanField, FloatField, TextField
import logging


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(50)')
    created_at = FloatField(default=time.time())


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


async def test(loop):
    await orm.create_pool(loop, user='root', password='123456', database='web')
    u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')
    print('dir',dir(u))
    await u.save()


async def find(loop):
    await orm.create_pool(loop, user='root', password='123456', database='web')
    rs = await User.findAll()
    print('查找测试： %s' % rs)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([test(loop), find(loop)]))
    loop.run_forever()
