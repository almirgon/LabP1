#coding: utf-8
#Crispiniano
#Unidade 4: Caixa Preta

n = int(raw_input())
condicao = True
cont = 0
for i in range(n):
	dados = raw_input().split()
	for j in range(3):
		if int(dados[j]) < 0 and condicao:
			if j == 0:
				print 'dado inconsistente. peso negativo.'
			elif j == 1:
				print 'dado inconsistente. combustível negativo.'
			else:
				print 'dado inconsistente. altitude negativa.'
			condicao = False
		if condicao:
			cont += 1
print '{} dados válidos.'.format(cont)
	
