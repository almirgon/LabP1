#coding: utf-8
#Crispiniano
#Unidade 4: Calcula DV

numero = raw_input()
par = 0
impar = 0
for i in range(len(numero)):
	if i % 2 == 0:
		par += int(numero[i])
	elif i % 2 != 0:
		impar += int(numero[i])

calculo = (par * impar) % 11 

if calculo == 10:
	print '{}-X'.format(numero)
else:
	 print '{}-{}'.format(numero,calculo)

	
