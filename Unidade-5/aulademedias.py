#coding: utf-8
#Crispiniano
#Unidade 5: Aula de Médias

soma = 0
cont = 0
lista = []
while True:
	numeros = float(raw_input())
	cont += 1
	soma += numeros
	lista.append(numeros)
	if soma >= 100:
		break

print 'Quantidade de números lidos: {}'.format(cont)
print 'Soma dos números lidos: {:.2f}'.format(soma)
print 'Média = {:.2f}'.format(soma/cont)

media = soma/cont

print '\nAbaixo da média'
for i in range(len(lista)):
	if lista[i] < media:
		print '{:.2f} ({}o)'.format(lista[i],i+1)
print '\nAcima da média'
for e in range(len(lista)):
	if lista[e] > media:
		print '{:.2f} ({}o)'.format(lista[e],e+1)
