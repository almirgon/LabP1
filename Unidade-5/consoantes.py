#coding: utf-8
#Crispiniano
#Unidade 5: Consoantes

lista = []
while True:
	palavra = raw_input()
	if palavra != '***':
		if palavra[0] not in 'aeiouAEIOU':
			lista.append(palavra[0])
	if palavra == '***':
		break

print 'Palavras: {}'.format(len(lista))
