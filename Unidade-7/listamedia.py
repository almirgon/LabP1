#coding: utf-8
#Crispiniano
#Unidade 7: Organiza Lista pela Média


def organiza_por_media(lista):
	soma = 0
	if len(lista) == 0:
		return []
	for i in lista:
		soma += i
	
	media = float(soma)/ len(lista)
	
	cont = 0
	cont2 = 0
	while cont < len(lista) - cont2:
		if lista[cont] > media:
			lista.append(lista.pop(cont))
			cont2 += 1
			cont -= 1
		cont += 1
	return lista 

p1 = [1,2,4,1,3,4,56,7,7,4,3,67]
assert organiza_por_media(p1) == [1,2,4,1,3,4,7,7,4,3,56,67]
