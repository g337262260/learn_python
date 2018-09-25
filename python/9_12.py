#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test moudle'

__author__ = 'Guowei'


class Student(object):
    def __init__(self, name, score, gender):
        self.__name = name
        self.__score = score
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender == 'male' or gender == 'female':
            self.__gender = gender
        else:
            print('Gender error')


if __name__ == '__main__':
    xiaomin = Student('XiaoMin', 100, 'male')
    print(xiaomin.get_gender())
