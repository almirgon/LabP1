#coding: utf-8
#Crispiniano
#Unidade 6: Caixa Registradora

def caixa_registradora(lista, meta):
	comissao = 0
	soma = 0
	string = ''
	resultados = []
	for i in range(len(lista)):
		soma += float(lista[i])
		if float(lista[i]) < 1000.0:
			comissao += float(lista[i]) * 0.05
		elif float(lista[i]) >= 1000.0 and float(lista[i]) < 5000.0:
			comissao += float(lista[i]) * 0.10
		elif float(lista[i]) >= 5000.0:
			comissao += float(lista[i]) * 0.15
	
	calculo = (soma - comissao)

	if calculo >= meta:
		string += 'Lucro'
	else:
		string += 'Prejuizo'

	resultados.append(soma)
	resultados.append(comissao)
	resultados.append(string)

	return resultados

assert caixa_registradora([1000.0, 2000.0, 5000.0, 2500.0, 950.0], 2000.0) == [11450.0, 1347.5, 'Lucro']
