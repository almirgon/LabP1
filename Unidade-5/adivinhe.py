#coding: utf-8
#Crispiniano
#Unidade 5: Adivinhe o número

import random

c = random.randint(1,10)
cont = 0
while True:
	palpite = int(raw_input('digite um numero: '))
	cont += 1
	if palpite == c:
		print 'Vc acertou em {} tentativas'.format(cont)
		break
	if palpite > c:
		print 'número muito alto, tente novamente'
	if palpite < c:
		print 'número muito baixo, tente novamente'
