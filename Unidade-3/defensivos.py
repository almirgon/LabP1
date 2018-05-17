#coding: utf-8
#Crispiniano
#Unidade 3: Defensivos

import math 

tipo = raw_input()
ha = float(raw_input())

if tipo == 'Fungicida':
	unidade = math.ceil(1.0 * ha/50)
	preco = unidade * 320
	print '{:.0f} Fungicida(s). {:.2f} reais.'.format(unidade,preco)
elif tipo == 'Herbicida':
	unidade = math.ceil(0.3 * ha/1)
	preco = unidade * 100
	print '{:.0f} Herbicida(s). {:.2f} reais.'.format(unidade,preco)
elif tipo == 'Inseticida':
	unidade = math.ceil(2.5 * ha/30)
	preco = unidade * 400
	print '{:.0f} Inseticida(s). {:.2f} reais.'.format(unidade,preco)

