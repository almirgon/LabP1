#coding: utf-8
#Crispiniano
#Unidade 6: Char único

def meu_count(sequencia, item):
	cont = 0
	for i in sequencia:
		if item == i:
			cont += 1
	return cont

def char_unico(string):
	string_nova = ""
	for caractere in string:
		if meu_count(string, caractere) == 1:
			string_nova += caractere
	return string_nova

assert char_unico("aa***xxxzzb+++") == "b"
assert char_unico("bbbbbbgkkkk") == "g"
	
