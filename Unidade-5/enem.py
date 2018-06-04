#coding: utf-8
#Crispiniano
#Unidade 5: ENEM

nome = []
nota = []

while True:
	entrada = raw_input().split()
	if entrada[0] == 'fim':
		break
	nome.append(entrada[0])
	nota.append(int(entrada[1]))
	
corte = int(raw_input())
condicao = True

for i in range(len(nome)):
	if nota[i] >= corte:
		print '{}, {}'.format(nome[i], nota[i])
		condicao = False
		
if condicao == True:
	print 'Nenhum candidato aprovado.'
