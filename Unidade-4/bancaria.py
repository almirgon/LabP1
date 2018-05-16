#coding: utf-8
#Crispiniano
#Unidade 4: Dígito Verificador de Conta Bancária

soma = 0

entrada = raw_input()

for i in range(len(entrada)):
	soma += int(entrada[i])

calculo = soma % 11

if calculo == 10:
	print '{}-X'.format(entrada)
else:
	print '{}-{}'.format(entrada,calculo)

