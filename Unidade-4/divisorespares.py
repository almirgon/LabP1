#coding: utf-8
#Crispiniano
#Unidade 4: Divisores Pares

n = int(raw_input())

for i in range(1,n+1):
	if n != i:
		if n % i == 0:
			if i % 2 == 0:
				print i 
