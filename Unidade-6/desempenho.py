#coding: utf-8
#Crispiniano
#Unidade 6: Melhor Desempenho

def melhor_desempenho(l):
	lista = [] 
	cont = 0
	for i in range(len(l)):
		for e in range(len(l[i])):
			if l[i][e] == '.':
				cont += 1
		lista.append(cont)
		cont = 0

	maior = 0
	for x in range(len(lista)):
		if int(lista[x]) >= maior:
			maior = lista[x]
	if maior == 0:
		return -1
	if maior != 0:
		for z in range(len(lista)):
			if int(lista[z]) == maior:
				return z
				

l = ['...**FFf','.fffff**','.****.ff']
assert melhor_desempenho(l) == 0

l = ['.','...','***']
assert melhor_desempenho(l) == 1

