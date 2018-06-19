#coding: utf-8
#Crispiniano
#Unidade 8: Agenda Ordenada

def ordenador(lista):
	while True:
		condicao = False
		for i in range(len(lista)-1):
			if lista[i] > lista[i+1]:
				lista[i], lista[i+1] = lista[i+1], lista[i]
				condicao = True
		if not condicao:
			break

nomes = []
while True:
	entrada = raw_input()
	if entrada == '####':
		break
	
	nomes.append(entrada)
	ordenador(nomes)
	for i in range(len(nomes)):
		if nomes[i] == entrada:
			print '* ' + nomes[i]
		else:
			print nomes[i]
	print '----'
