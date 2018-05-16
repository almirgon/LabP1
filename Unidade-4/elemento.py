#coding: utf-8
#Crispiniano
#Unidade 4: Encontra elemento

numero = raw_input()
seq = raw_input().split()
condicao = False

for i in range(len(seq)):
	if numero == seq[i]:
		condicao = True

if condicao:
	print 'sim'
else:
	print 'não'
