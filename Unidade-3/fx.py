#coding: utf-8
#Crispiniano
#Unidade 3: f(x)

x = int(raw_input())

if abs(x) <= 1:
	print '1'
elif 1 < abs(x) <= 2:
	print '2'
elif 2 < abs(x) <= 3:
	print'{}'.format(x**2)
elif abs(x) > 3:
	print '{}'.format(x**3)
