#coding: utf-8
#Crispiniano
#Unidade 6: Multiplica Lista

def multiplica_lista(n,lista):
	if n == 0:
		return []
	else:
		return n * lista 

l = ['joao', 'pedro']
assert multiplica_lista(2,l) == ['joao', 'pedro', 'joao', 'pedro']
