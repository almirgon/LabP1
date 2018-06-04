#coding: utf-8
#Crispiniano
#Unidade 5: Câmbio

while True:
	entrada = raw_input().split()
	if entrada[0] == 'fim':
		break
	if entrada[3] == 'U$':
		dinheiro = float(entrada[1])
		saida = dinheiro * 0.49
		print 'R$ {:.2f} = U$ {:.2f}'.format(dinheiro,saida)
	if entrada[3] == '$':
		dinheiro = float(entrada[1])
		saida = dinheiro * 2.58
		print 'R$ {:.2f} = $ {:.2f}'.format(dinheiro,saida)
	if entrada[3] == '€':
		dinheiro = float(entrada[1])
		saida = dinheiro * 0.38
		print 'R$ {:.2f} = € {:.2f}'.format(dinheiro,saida)
