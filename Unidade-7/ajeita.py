#coding: utf-8
#Crispiniano
#Unidade 7: Ajeita Lista de Números Inteiros

def ajeita_lista(dados):
	while True:
		condicao = False
		for i in range(len(dados)-1):
			if dados[i] < dados[i+1]:
				dados[i], dados[i+1] = dados[i+1], dados[i]
				condicao = True
		if not condicao:
				break
	
	for x in range(len(dados)-1,-1,-1):
		if dados[x] % 2 != 0:
			dados.append((dados.pop(x)))

lista1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
assert ajeita_lista(lista1) == None
assert lista1 == [8, 6, 4, 2, 1, 3, 5, 7, 9]
