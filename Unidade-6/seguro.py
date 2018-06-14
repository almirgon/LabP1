#coding: utf-8
#Crispiniano
#Unidade 6: Cálculo de Seguro

def calcula_seguro(valor, lista):
	pontuacao = 0
	
	if lista[0] <= 21 or lista[0] > 60:					
		pontuacao += 20
	elif  22 <= lista[0] <= 30:
		pontuacao += 15
	elif  31 <= lista[0] <= 40:
		pontuacao += 12
	elif  41 <= lista[0] <= 60:
		pontuacao += 10

	if lista[1] == True:
		pontuacao += 10
	else:
		pontuacao += 20
	
	if lista[2] == True:
		pontuacao += 20
	else:
		pontuacao += 10
	
	if lista[3] == True:
		pontuacao += 20
	else:
		pontuacao += 10
	
	if lista[4] == True:
		pontuacao += 20
	else:
		pontuacao += 10
	
	if lista[5] == True:
		pontuacao += 10
	else:
		pontuacao += 20
		
	if lista[6] == 'Lazer' or lista[6] == 'Misto':
		pontuacao += 20
	else:
		pontuacao += 10
		
	
	if pontuacao <= 80:                          
		risco = 'Risco Baixo'
		preco = 0.1 * valor
	elif 80 < pontuacao <= 100:		
		risco = 'Risco Medio'
		preco = 0.2 * valor
	else:
		risco = 'Risco Alto'	
		preco = 0.3 * valor
	
	
	saida = []
	saida.append(pontuacao)
	saida.append(risco)
	saida.append(preco)
	
	return saida

assert calcula_seguro(2000.0, [21, True, True, True, True, True, 'Misto']) == [120, "Risco Alto", 600.0]
