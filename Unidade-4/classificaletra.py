#coding: utf-8
#Crispiniano
#Unidade 4: Classifica Letra

palavra = raw_input()
vogais = 'aeiouAEIOU'
for i in range(len(palavra)):
	if palavra[i] in vogais:
		print '<{}> sim'.format(palavra[i])
	else:
		print '<{}> nao'.format(palavra[i])
