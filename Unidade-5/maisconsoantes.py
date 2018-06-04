#coding: utf-8
#Crispiniano
#Unidade 5: Mais Consoantes

cont = 0
while True:
	vogais = 0
	consoantes = 0
	palavras = raw_input()
	cont += 1
	for i in range(len(palavras)):
		if palavras[i] in 'aeiouAEIOU':
			vogais += 1
		else:
			consoantes += 1
	if consoantes > vogais:
		print cont 
		break
	
