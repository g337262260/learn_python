#!user/bin/env python3
# -*- coding:utf-8 -*-

"""wsgi"""

__author__ = 'Guowei'

def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][2:] or 'web')
    return [body.encode('utf-8')]