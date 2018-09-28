#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration,把default的host 替换成override的host
'''

__author__ = 'Guowei'

import config_default


class Dict(dict):
    """
      重写属性设置，获取方法
      支持通过属性名访问键值对的值，属性名将被当做键名
      """
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        print('names--', names)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


def merge(defaults, override):
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r


def toDict(d):
    D = Dict()
    for k, v in d.items():
        D[k] = toDict(v) if isinstance(v, dict) else v
        return D


configs = config_default.configs

try:
    import config_override

    configs = merge(configs, config_override.configs)
except ImportError:
    pass

configs = toDict(configs)

if __name__ == '__main__':
    a= {'name','age'}
    b = {'lili',8}
    d = Dict(a,b)
