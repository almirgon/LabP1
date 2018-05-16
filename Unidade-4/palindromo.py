#coding: utf-8
#Crispiniano
#Unidade 4: Palíndromo

entrada = raw_input()

invertida = ''
palavra = ''
for e in range(len(entrada)):
	if entrada[e] != ' ':
		palavra += entrada[e]

for i in range(len(palavra)-1,-1,-1):
	invertida += palavra[i]

if palavra == invertida:
	print '{} é palíndromo'.format(entrada)
else:
	print '{} não é palíndromo'.format(entrada)
	
