#coding: utf-8
#Crispiniano
#Unidade 5: Mais Consoantes

palavras = []
while True:
	palavra = raw_input()
	
	if palavra == 'fim':
		break
	
	palavras.append(palavra)

letra = raw_input()
numero = int(raw_input())


ocorrencias = []
for p in palavras:
	cont = 0
	
	for l in p:
		if l == letra:
			cont += 1
			
	if cont > numero:
		ocorrencias.append(p)

if len(ocorrencias) == 0:
	print 'Nenhuma palavra encontrada.'

else:
	for o in ocorrencias:
		print o
