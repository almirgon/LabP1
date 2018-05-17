#coding: utf-8
#Crispiniano
#Unidade 4: Assembleia

n = int(raw_input())

sim = 0
nao = 0
for i in range(n):
	votos = raw_input()
	if votos == 'sim':
		sim += 1
	elif votos == 'não':
		nao += 1

validos = sim + nao 

if validos <= (n/2):
	print 'Quorum insuficiente.'
elif sim > nao:
	print 'Decisão a favor da greve.'
elif sim < nao:	
	print 'Decisão contrária à greve.'
else:
	print 'Empate.'
