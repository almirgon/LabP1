#coding: utf-8
#Crispiniano
#Unidade 3: Depois do 13

n1 = int(raw_input())
n2 = int(raw_input())
n3 = int(raw_input())

if n1 == 13:
	print '0'
elif n2 == 13:
	print n1
elif n3 == 13:
	if n1 + n2 != 13:
		print n1 + n2
	else:
		print '0'
elif n1 + n2 == 13:
	print '0'
else:
	print n1+n2+n3		
