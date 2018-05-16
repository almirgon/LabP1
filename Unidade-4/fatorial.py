#coding: utf-8
#Crispiniano
#Unidade 4: Fatorial

n = int(raw_input())

fatorial = 1
lista = []
for i in range(n,0,-1):
	lista.append(i)

for e in range(len(lista)):
	fatorial *= int(lista[e])

print fatorial
