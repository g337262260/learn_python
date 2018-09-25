# -*- coding: utf-8 -*-
#-------------practise1------------------

#序列生成器
def _odd_iter():
    n = 1
    while True:
        n = n + 1
        yield n
#筛选函数
def _not_huishu(n):
	return str(n) == str(n)[::-1] 
#生成器
def is_palindrome():
    yield 1
	it = _odd_iter()
	while True:
		n = next(it)
		yield n 
		it = filter(_not_huishu(n),it)
for n in is_palindrome():
	if n <100:
		print(n)
	else:
		break
	
def createCounter():
	def f(j):
		def counter():
			return j+1
	fs = []
	for i in range(1,6):
		fs.append(f(i))
	return fs
	


	
	



