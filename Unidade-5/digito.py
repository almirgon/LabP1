#coding: utf-8
#Crispiniano
#Unidade 5: Dígito por dígito

n = int(raw_input())

x = n
lista = []
while True:
	lista.append(x%10)
	x = x/10
	if len(lista) == len(str(n)):
		for k in lista:
			print k 
		break
