#coding: utf-8
#Crispiniano
#Unidade 8: Acima de

def acima_de(n, l):
	lista = []
	for i in range(len(l)):
		if int(l[i]) > int(n):
			lista.append(i)
	return lista


