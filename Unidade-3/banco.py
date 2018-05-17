#coding: utf-8
#Crispiniano
#Unidade 3: Caixas em Banco

import math

cpf = int(raw_input())

calculo = 1 + int(25 * (cpf * math.pi % 1))

if 1 <= calculo <= 8:
	print 'Caixa {}, térreo'.format(calculo)
elif 9 <= calculo <= 20:
	print 'Caixa {}, primeiro andar'.format(calculo)
elif 21 <= calculo <= 30:
	print 'Caixa {}, segundo andar'.format(calculo)
