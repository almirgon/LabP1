#coding: utf-8
#Crispiniano
#Unidade 5: Bingo!
jogador1 = raw_input().split()
jogador2 = raw_input().split()

while True:
	n = raw_input()
	for i in range(len(jogador1)-1,-1,-1):
		if jogador1[i] == n:
			jogador1.pop(i)
	for e in range(len(jogador2)-1,-1,-1):
		if jogador2[e] == n:
			jogador2.pop(e)
	if len(jogador1) == 0 and len(jogador2) == 0:
		print 'Empate.'
		break
	elif len(jogador1) == 0:
		print 'Bingo! Jogador 1 venceu.'
		break
	elif len(jogador2) == 0:
		print 'Bingo! Jogador 2 venceu.'
		break
