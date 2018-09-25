#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""多线程和多进程"""

__author__ = 'Guowei'
from multiprocessing import Process, Pool
import subprocess
import os, time, random
import re


def run_poc(name):
    print('Run child process %s (%s)' % (name, os.getpid()))


def test1():
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_poc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s run %0.2f seconds' & (name, end - start))


def test2():
    print('Parent process %s .' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done ..')
    p.close()
    p.join()
    print('All subprocesses done ')


def test3():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit cede:', r)


def is_valid_email(addr):
    if re.match(r'^\w+.*\w+@\w+\.com$', addr):
        return True
    else:
        return False
def name_of_email(addr):
    result = re.match(r'([<\w+\s?\w+>]*\s?\w+.*\w+)@(\w+).com$', addr)
    g = result.group(1)
    if result is not None:
        if '<' in g and '>' in g:
            print("Split",g.split('<')[1].split('>')[0])
            return g
        else:
            return g






if __name__ == '__main__':
    print('valid_result',   name_of_email('<Tom Paris> tom@voyager.com'))
