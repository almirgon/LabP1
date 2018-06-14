#coding: utf-8
#Crispiniano
#Unidade 6: A Primeira Letra em Caixa Alta

def caixa_alta(frase):
	frase += ' '
	nova_frase = ''
	frase_final = ''
	cont = 0

	for i in range(len(frase)):
		if frase[i] != " ":
			cont += 1
		elif frase[i] == ' ' and cont > 1:
			frase_final += frase[i - cont].upper()
			for j in range((i - (cont - 1)), i):
				frase_final += frase[j]
			frase_final += ' '
			cont = 0
		elif frase[i] == ' ' and cont == 1:
			frase_final += frase[i - cont].lower()
			frase_final += ' '
			cont = 0
		elif frase[i] == ' ' and cont == 0:
			frase_final += ' '

	for index in range(len(frase_final)-1):
		nova_frase += frase_final[index]

	return nova_frase

assert caixa_alta("A primeira letra de cada palavra") == "a Primeira Letra De Cada Palavra"
