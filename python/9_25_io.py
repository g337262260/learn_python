#!user/bin/env python3
# -*- coding:utf-8 -*-

"""io"""

__author__ = 'Guowei'


import asyncio

@asyncio.coroutine
def hello():
    print('Hello,World')
    r = yield from asyncio.sleep(1)
    print('Hello again')




def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


@asyncio.coroutine
def wget(host):
    print('wget %s ---' % host)
    connect = asyncio.open_connection(host,80)
    reader,writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
        # Ignore the body, close the socket
    writer.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(hello())
    # loop.close()
    tasks = [wget(host) for host in ['www.sina.com.cn','www.sohu.com','www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
