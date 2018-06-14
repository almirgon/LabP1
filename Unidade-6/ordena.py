#coding: utf-8
#Crispiniano
#Unidade 6: Ordena Tipos

def ordena_tipos(lista):
	inteiros = []
	letras = []
	outros = []
	for i in lista:
		if i.isdigit():
			inteiros.append(i)
		elif i.isalpha():
			letras.append(i)
		else:
			outros.append(i)

	return inteiros + letras + outros 
	
	
assert ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8']) == ['2', '4', '8', 'e', '1a', '4.4', 'e6']
