#coding: utf-8
#Crispiniano
#Unidade 4: Número Mágico
n = int(raw_input())

lista = []
for i in range(n):
	elementos = int(raw_input())
	lista.append(elementos)


controle = 1
resultado = 0
for x in range(len(lista)-1,-1,-1):
	if controle:
		resultado += int(lista[x])
		controle = 0
	else:
		resultado -= int(lista[x])
		controle = 1
print resultado
