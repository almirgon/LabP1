#coding: utf-8
#Crispiniano
#Unidade 6: Primeiro Número Acima

def primeiro_numero_acima(numeros):
	soma = 0
	for i in range(len(numeros)):
		soma += numeros[i]

	media = float(soma)/len(numeros)


	for e in range(len(numeros)):
		if numeros[e] > media:
			return e + 1
			break
	else:
		return -1 

numeros = [4, 5, 6, 7, 8]
assert primeiro_numero_acima(numeros) == 4

numeros = [6, 4, 5]
assert primeiro_numero_acima(numeros) == 1
