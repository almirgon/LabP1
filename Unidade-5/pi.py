#coding: utf-8
#Crispiniano
#Unidade 5: Pi

while True:
	saida = 0
	n = int(raw_input())
	if n == 0:
		break
	cont = 0
	var = 1
	for i in range(n):
		if cont % 2 != 0:
			saida -= (1.0/float(var))
		else:
			saida += (1.0/float(var))
		cont += 1
		var += 2
	print '{:.6f}'.format(4 * saida)
