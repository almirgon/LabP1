#coding: utf-8
#Crispiniano
#Unidade 5: Média Atinge Limite

cont = 0
soma = 0
lista = []
while True:
	entrada = raw_input()
	if entrada == '-':
		break
	if entrada != '-':
		cont += 1
		soma += float(entrada)
		lista.append(float(soma/cont))
limite = float(raw_input())
alcancado = False
for i in range(len(lista)):
	if lista[i] > limite:
		print 'media = {:.1f}'.format(lista[i])
		print 'num = {}'.format(i+1)
		alcancado = True
		break
if not alcancado:
	print 'limite não alcançado'
