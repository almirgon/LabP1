#coding: utf-8
#Crispiniano
#Unidade 4: Dígito mais frequente

n = int(raw_input())

lista = [0,0,0,0,0,0,0,0,0,0,0]
for i in range(n):
	numeros = raw_input()
	for e in range(len(numeros)):
		lista[int(numeros[e])] += 1

maior = 0
for x in range(len(lista)):
	if lista[x] > maior:
		maior = lista[x]

for t in range(len(lista)):
	if lista[t] == maior:
		print t,maior
		break
