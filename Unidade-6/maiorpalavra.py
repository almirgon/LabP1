#coding: utf-8
#Crispiniano
#Unidade 6: Maior Palavra de Uma Frase

frase = 'eu acredito que seja um bom exemplo'

def meu_split(lista):
    l = []
    aux = ''
    for k in range(len(lista)):
        if lista[k] != ' ':
            aux += lista[k]
        if lista[k] == ' ' or k == len(lista) - 1:
            l.append(aux)
            aux = ''
    return l

def maior_palavra(frase):
	palavras = meu_split(frase)
	maior_palavra = ''
	for palavra in palavras:
		if len(palavra) >= len(maior_palavra):
			maior_palavra = palavra
	return maior_palavra
	

assert maior_palavra("eu acredito que seja um bom exemplo") == "acredito"
