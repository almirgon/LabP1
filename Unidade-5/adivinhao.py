#coding: utf-8
#Crispiniano
#Unidade 5: Adivinhão

alvo = int(raw_input())
cont = 0
while True:
	numeros = int(raw_input())
	cont += 1
	if abs(numeros - alvo) > 100:
		print 'Não acertou o número alvo {}! Foi eliminado com {} tentativa(s).'.format(alvo,cont)
		break
	if numeros == alvo:
		print 'Acertou o número alvo {}! Ganhou com {} tentativa(s).'.format(alvo,cont)
		break
