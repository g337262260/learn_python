# -*- coding: utf-8 -*-

#def trim(str):
#	while str[0] ==' ':
#		str = str[1:]
#	while str[-1] == ' ':
#		str = str[-1:]
	
#	return str
	
#s = input('请输入一个字符串')
#print(trim(s))

def findMinAndMax(L):
	max = L[0]
	min = L[0]
	for x in L :
		if min >x :
			min = x
		if max <x :
			max = x
	return (min,max)
print(findMinAndMax([1,2,4,5,7,3]))

		
	
	



