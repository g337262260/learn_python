# -*- coding: utf-8 -*-

import math
 
def quadratic(a,b,c):
	deta = math.pow(b,2)-4*a*c
	if a ==0 or deta <0:
		print('方程没有解')
	elif deta==0:
		x1 = x2 = -b/(2*a)
		print('方程有两个相同的解为：x1=%s ,x2 =%s' %(x1,x2))
		return x1,x2
	elif deta>0:
		s = math.sqrt(deta)
		x1 = ((-b)+s)/(2*a)
		x2 = ((-b)-s)/(2*a)
		print('方程有两不同的解为：x1=%s ,x2 =%s' %(x1,x2))
		return x1,x2
		
	
a= int(input('请输入a的值：'))	
b= int(input('请输入b的值：'))	
c= int(input('请输入c的值：'))	
print(quadratic(a,b,c))