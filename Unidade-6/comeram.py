#coding: utf-8
#Crispiniano
#Unidade 6: Quantos Comeram?

def quantos_comeram(N, fila):
	acumulador = 0
	for i in range(len(fila)):
		if fila[i] <= N:
			acumulador += fila[i]
			N -= fila[i]
		else:
			break
	return acumulador

assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5
