#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test moudle'

__author__ = 'Guowei'
import unittest
import sys
import os

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError('Value Error')
        if self.score <= 60:
            return 'C'
        if self.score <= 80:
            return 'B'
        return 'A'

def findFile(path,key):
    cur_path = os.path.abspath(path)
    list = []
    for f in os.listdir(cur_path):
        file_path = os.path.join(path,f)
        if os.path.isfile(file_path):
            if file_path.find(key) != -1:
                list.append(file_path)
        else:
            sub = findFile(file_path,key)
            for l in sub:
                list.append(l)
    return list


if __name__ == '__main__':
    dir_list = findFile('C:\\Users\\Administrator\\Desktop','png')
    for d in dir_list:
        print(d)