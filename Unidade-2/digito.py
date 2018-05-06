#coding: utf-8
#Crispiniano
#Unidade 2: Dígito Verificador de 5 Dígitos

digito = raw_input()
soma = 0
for i in range(len(digito)):
	soma += int(digito[i])

verificador = soma % 11 

print '{}-{:02.0f}'.format(digito,verificador)
