#coding: utf-8
#Crispiniano
#Unidade 7: Afinidade Musical

def meu_in(elemento,lista):
	for e in lista:
		if e == elemento:
			return True
	return False

def tem_afinidade(l1, l2):
	cont = 0
	for i in l1:
		for x in l2:
			if i == x:
				cont += 1
	if cont >= 3:
		return True
	else:
		return False

l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'u2', 'jquest']
assert tem_afinidade(l1, l2) == True
	
