#coding: utf-8
#Crispiniano
#Unidade 4: Bolsa do CNPq

saldo = 0
maior_saldo = 0
maior_mes = 0

for i in range(12):
	saldo += 500 - int(raw_input())
	if saldo < 0:
		saldo = 0 
	elif saldo >= maior_saldo:
		maior_saldo = saldo
		maior_mes = i

print ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'][maior_mes]
