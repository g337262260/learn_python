#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""datetime、collection、struct"""

__author__ = 'Guowei'
import re
from datetime import datetime, timezone, timedelta
import base64
import hashlib
import hmac
import itertools


def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    g = re.match(r'^UTC((-|\+)?\d+):00$', tz_str)
    if g.group(1)[0] == '+':
        hour = int(g.group(1)[1:])
    else:
        hour = -int(g.group(1)[1:])
    print(hour)
    tz = timezone(timedelta(hours=hour))
    return cday.replace(tzinfo=tz).timestamp()


def safe_base64_decode(s):
    while len(s) % 4 != 0:
        # 代表的是byte
        s += b'='
        print('s:', s)
    return base64.b64decode(s)


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    md5 = hashlib.md5()
    # 加盐
    md5.update((password + user).encode('utf-8'))
    if db[user] == md5.hexdigest():
        return '登录成功'
    else:
        return '密码错误'


def hmac_test(name, password):
    h = hmac.new(name.encode('UTF=8'), password.encode('UTF-8'), digestmod='MD5')
    return h.hexdigest()


from functools import reduce


def pi(N):
    # 创建奇数数列
    natuals = itertools.count(1, 2)
    # 获取数列的前N项
    ns = itertools.takewhile(lambda x: x <= 2 * N - 1, natuals)
    # 用4除并添加正负号,并求和
    # 笨办法
    # index = 0
    # ji_sum = 0
    # for n,m in ns,:
    #     if index % 2 == 0:
    #         n = 4 / n
    #     else:
    #         n = -4 / n
    #     index += 1
    #     ji_sum += n
    # 高级办法
    fuhao = itertools.cycle([1, -1])
    data = map(lambda x, y: 4.0 * y / x, list(ns), fuhao)
    ji_sum = reduce(lambda x, y: x + y, data)
    return ji_sum


class Query(object):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('End')

    def query(self):
        print('Query info about %s...' % self.name)


from contextlib import closing
from urllib import request
import json

if __name__ == '__main__':
    with request.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json') as page:
        data = page.read()
        print('Status',page.status,page.reason)
        for k,v in page.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', json.loads(data.decode('utf-8')))