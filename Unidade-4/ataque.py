#coding: utf-8
#Crispiniano
#Unidade 4: Melhor Ataque

n = int(raw_input())

lista_nome = []
lista_gol = []
soma = 0
maior = 0 
for i in range(1,n+1):
	nome = raw_input()
	gols = int(raw_input())
	if gols > maior:
		maior = gols 
	lista_nome.append(nome)
	lista_gol.append(gols)
	soma += gols 

print 'Time(s) com melhor ataque ({} gol(s)):'.format(maior)

for n in range(len(lista_gol)):
	if lista_gol[n] == maior:
		print lista_nome[n]

print '\nMédia de gols marcados: {:.1f}'.format(soma/float(len(lista_gol)))
	
