#coding: utf-8
#Crispiniano
#Unidade 6: Get Itens 

def get_items(valores, indices):
	l=[]
	for i in indices:
		if i > len(valores)-1:
			l.append(None)
		else:
			l.append(valores[i])
	return l

valores = [18, 22, 73, 32, 19, 21, 43]
indices = [3, 4, 8, 1]
assert get_items(valores, indices) == [32, 19, None, 22]
