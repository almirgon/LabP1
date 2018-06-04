#coding: utf-8
#Crispiniano
#Unidade 5: Fundo de Investimento

soma = 0
cont = 0
lista = []
while True:
	fundo = float(raw_input())
	cont += 1
	soma += fundo
	media = soma/cont 
	lista.append(fundo)
	if fundo < media:
		break

nova_soma = 0

for i in range(len(lista)):
	if i != len(lista)-1:
		nova_soma += lista[i]
print 'Saldo total do FIS: R${:.2f}.'.format(nova_soma)
print 'Média das contribuições: R${:.2f}.'.format(nova_soma/(len(lista)-1))
