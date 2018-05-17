#coding: utf-8
#Crispiniano
#Unidade 4: B2 para B10

decimal = raw_input()
soma = 0

for i in range(len(decimal)):
	exp = len(decimal)- i - 1
	numero = 2 ** exp
	resultado = int(decimal[i]) * numero
	soma += resultado
	print '{} * {} = {}'.format(decimal[i],numero,resultado)

print '{}(2) = {}(10)'.format(decimal,soma)
