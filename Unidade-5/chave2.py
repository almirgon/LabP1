#coding: utf-8
#Crispiniano
#Unidade 5: Chave

chave = raw_input()
i = 0
contador = 0
contador2 = 0
condicao_auxiliar = True

while True:
	contador2 += 1
	
	if chave[i] == chave[i+1] == chave[i+2]:
		print 'Chave insegura. 3 caracteres consecutivos iguais.'
		condicao_auxiliar = False
		break
	
	if chave[i] in 'aeiouAEIOU':
		contador += 1
	
	if contador > 5:
		print 'Chave insegura. 6 vogais.'
		condicao_auxiliar = False
		break
	
	if i < len(chave) -3:
		i += 1

	if contador2  == len(chave):
		break	
if condicao_auxiliar == True:
	print 'Chave segura!'
