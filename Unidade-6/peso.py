#coding: utf-8
#Crispiniano
#Unidade 6: Peso Ideal

def calculaPeso(sexo, altura):
	if sexo == 'f' or sexo == 'F':
		peso = 62.1 * altura - 44.7
	else:
		peso = 72.7 * altura - 58
	return peso

while True:
	entrada = raw_input()
	
	if entrada == '****':
		break
	
	entrada = entrada.split()
	sexo = entrada[0]
	altura = float(entrada[1])
	peso = calculaPeso(sexo, altura)
	if sexo == 'f' or sexo == 'F':
		print 'Mulher: peso ideal é {:.1f}'.format(peso)
	else:
		print 'Homem: peso ideal é {:.1f}'.format(peso)
