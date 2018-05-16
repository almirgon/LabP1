#coding: utf-8
#Crispiniano
#Unidade 4: Descarta coincidentes

n = int(raw_input())
lista_aceitos = []
lista_descartados = []

for i in range(n):
	numeros = raw_input()
	for e in range(len(numeros)):
		if int(numeros[e]) == e:
			lista_descartados.append(numeros)
			break 
	else:
		lista_aceitos.append(numeros)

print '---'

print '{} aceito(s)'.format(len(lista_aceitos))

for a in range(len(lista_aceitos)):
	print lista_aceitos[a]
print '{} descartado(s)'.format(len(lista_descartados))

for d in range(len(lista_descartados)):
	print lista_descartados[d]
