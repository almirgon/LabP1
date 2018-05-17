#coding: utf-8
#Crispiniano
#Unidade 4: Conta Divisíveis

k = int(raw_input())
n = int(raw_input())
cont = 0
for i in range(n):
	valores = int(raw_input())
	if valores % k == 0:
		cont += 1

porcentagem = float(cont * 100)/n

print '{} ({:.1f}%)'.format(cont,porcentagem)
