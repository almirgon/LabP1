#coding: utf-8
#Crispiniano
#Unidade 6: Calcula Verificador

def calcula_verificador(n):
	digito = str(n)
	soma = 0
	for i in range(len(digito)):
		soma += int(digito[i])
		if soma >= 19:
			break

	calculo = soma % 11
	resultado = ''

	if calculo == 0:
		resultado = 'a'
	elif calculo == 1:
		resultado = 'b'
	elif calculo == 2:
		resultado = 'c'
	elif calculo == 3:
		resultado = 'd'
	elif calculo == 4:
		resultado = 'e'
	elif calculo == 5:
		resultado = 'f'
	elif calculo == 6:
		resultado = 'g'
	elif calculo == 7:
		resultado ='h'
	elif calculo == 8:
		resultado = 'i'
	elif calculo == 9:
		resultado = 'j'
	elif calculo == 10:
		resultado = 'k'
	
	return resultado

n = 9934
m = 1234123
assert calcula_verificador(n) == "k"
assert calcula_verificador(m) == "f"
