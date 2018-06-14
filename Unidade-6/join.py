#coding: utf-8
#Crispiniano
#Unidade 6: Meu join

def meu_join(delimitador, sequencia_de_string):
	nova = ''
	for i in range(len(sequencia_de_string)):
		if i == len(sequencia_de_string)-1:
			nova += sequencia_de_string[i]
		else:
			nova += sequencia_de_string[i] + delimitador
	return nova 

assert meu_join("*", "abc") == "a*b*c"
assert meu_join("*", ["a", "b", "c"]) == "a*b*c"
