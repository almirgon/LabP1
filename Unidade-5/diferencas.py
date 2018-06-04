#coding: utf-8
#Crispiniano
#Unidade 5: Diferenças

soma = 0
cont = 0
sub = 0
lista = []
while True:
	n1,n2 = raw_input().split()
	numero1 = int(n1)
	numero2 = int(n2)
	if n1 != '0' or n2 != '0':
		if numero2 > 0:
			sub = abs(numero1 - numero2)
		if numero2 <= 0:
			sub = abs(numero1 + abs(numero2))
		lista.append(sub) 
		soma += sub
		cont += 1
		media = float(soma)/cont
	if n1 == '0' and n2 == '0':
		break 

for i in range(len(lista)):
	if float(lista[i]) > media:
		print i+1
