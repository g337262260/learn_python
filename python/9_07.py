# -*- coding: utf-8 -*-
#-------------practise1------------------
from functools import reduce

name = ['adam', 'LISA', 'barT']
def normalize(name):
	name = name[0].upper()+name[1:].lower()
	return name
print(list(map(normalize,name)))

#-------------practise2---------------------
L = [5,2,3,4]

def fn(x,y):
	return x*y
def prod(L):
	return reduce(fn,L)
print(prod(L))
	
#-------------practise3---------------------	
s = '123.456'
def fn1(x,y):
	return (x*10+y)
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
	
def str2float(s):
	i = s.index('.')
	s = s[0:i]+s[i+1:]
	return reduce(fn1,map(char2num,s))/1000
print(str2float(s))
#-------------practise4---------------------

	
	



