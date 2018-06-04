#coding: utf-8
#Crispiniano
#Unidade 5: Abaixo da média

lista = []
soma = 0
cont = 0
while True:
	numeros = raw_input()
	if numeros == 'fim':
		break
	if numeros != 'fim':
		soma += float(numeros)
		cont += 1
		lista.append(float(numeros))

media = soma/cont
print '{:.2f}'.format(media)

for i in range(len(lista)):
	if lista[i] < media:
		print '{} {:.0f}'.format(i+1,lista[i])
