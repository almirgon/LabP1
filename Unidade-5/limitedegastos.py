#coding: utf-8
#Crispiniano
#Unidade 5: Limite açude

limite = float(raw_input())

medias_acima = []
while True:
	entrada = raw_input()
	valores = entrada.split()
	soma = 0.0
	
	string = ''
		
	for e in range(len(valores)):
		if valores[e] != 'fim':
			if e == (len(valores)-1):
				string  += str(float(valores[e]))
			else:
				string += str(float(valores[e])) + ' '
				
			soma += float(valores[e])
			
		media = soma / len(valores)
	
	if float(media) > limite:
		print string
		
	elif float(media) <= limite / 2:
		break
	
	if valores[0] == 'fim':
		break
