#coding: utf-8
#Crispiniano
#Unidade 7: Acordes aprendidos

def meu_in(elemento,lista):
	for i in lista:
		if i == elemento:
			return True
	return False


def acordes(m1, m2):
	lista = []

	lista += m1
	for i in m2:
		if meu_in(i,m1) == False:
			lista.append(i)

	return lista 
		
m1 = ['c', 'd', 'dm']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'dm', 'a']
assert m1 == ['c', 'd', 'dm']
assert m2 == ['c', 'a']

m1 = ['c', 'd']
m2 = ['c', 'a']
assert acordes(m1, m2) == ['c', 'd', 'a']
