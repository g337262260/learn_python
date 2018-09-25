
w = input('请输入体重 :')
l = input('请输入身高 :')
bmi = (int(w)/(float(l)*float(l)))
if bmi<18.5:
	print('体重过轻')
elif bmi<25:
	print('正常')
elif bmi<28:
	print('过重')
elif bmi<32:
	print('肥胖')
else:
	print('严重肥胖')
