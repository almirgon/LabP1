#coding: utf-8
#Crispiniano
#Unidade 8: Agrupa Múltiplos


def agrupa_multiplos(seq, k):
	cont = 0
	for i in range(len(seq)):
		if seq[i] % k == 0:
			x = seq[i]
			for e in range(i,cont,-1):
				seq[e] = seq[e-1]
			seq[cont] = x
			cont += 1

seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]

# agrupando seq por múltiplos de 5
agrupa_multiplos(seq, 5)
assert seq == [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]

# reagrupando por pares
agrupa_multiplos(seq, 2)
assert seq == [10, 6, 12, 6, 8, 14, 15, 25, 3, 1, 7]	

