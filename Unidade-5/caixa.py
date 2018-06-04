#coding: utf-8
#Crispiniano
#Unidade 5: Caixa preta

peso_cont = 0
combustivel_cont = 0
altitude_cont = 0
while True:
	teve_negativo = False
	ca = raw_input().split()
	peso_cont += 1
	combustivel_cont += 1
	altitude_cont += 1
	for i in range(len(ca)):
		if int(ca[i]) < 0:
			if i == 0:
				print 'dado inconsistente. peso negativo.'
				peso_cont -= 1
				combustivel_cont -= 1
				altitude_cont -= 1
			if i == 1:
				print 'dado inconsistente. combustível negativo.'
				combustivel_cont -= 1
				altitude_cont -= 1
			if i == 2:
				print 'dado inconsistente. altitude negativa.'
				altitude_cont -= 1
			teve_negativo = True
			break
	if teve_negativo:
		break
print 'peso: {}'.format(peso_cont)
print 'combustível: {}'.format(combustivel_cont)
print 'altitude: {}'.format(altitude_cont)
