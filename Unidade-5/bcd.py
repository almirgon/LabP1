#coding: utf-8
#Crispiniano
#Unidade 5: BCD
while True:
	parte1 = ''
	parte2 = ''
	n = raw_input()
	if len(n) == 8:
		for i in range(len(n)):
			if i < 4:
				parte1 += n[i]
			else:
				parte2 += n[i]
		numberEx1 = int(parte1,2)
		numberEx2 = int(parte2,2)
		num = str(numberEx1) + str(numberEx2)
		if len(num) == 2:
			print num
		else:
			print 'BCD inválido.'
	elif n != 'fim':
		print 'Tente novamente.'
		
	if n == 'fim':
		break
