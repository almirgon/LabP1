#coding: utf-8
#Crispiniano
#Unidade 5: Guerra Baralho

jogador1 = 0
jogador2 = 0
empate = 0
while True:
	entrada = raw_input().split()
	if int(entrada[0]) == 0 and int(entrada[1]) == 0:
		break
	if int(entrada[0]) > int(entrada[1]):
		jogador1 += 1
	if int(entrada[0]) < int(entrada[1]):
		jogador2 += 1
	if int(entrada[0]) == int(entrada[1]):
		empate += 1
	
print 'Jogador 1: {}, Jogador 2: {}, Empates: {}'.format(jogador1,jogador2,empate)
