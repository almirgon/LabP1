#coding: utf-8
#Crispiniano
#Unidade 6: Analytics Votação

def conta_votos(votacao,id):
	votos_sim = 0
	votos_nao = 0
	saida = []
	
	for elemento in votacao:
		elemento = elemento.split(',')
		if elemento[1] == str(id):
			if elemento[4] == 'sim':
				votos_sim += 1
			else:
				votos_nao += 1
	saida.append(votos_sim)
	saida.append(votos_nao)
	return saida
	
votacao = []
votacao.append('lei sobre bancos,543,joao,PPPP,sim')
votacao.append('lei sobre bancos,543,marina,PPPP,nao')
votacao.append('lei maria da penha,5,joao,PPPP,sim')
votacao.append('lei sobre bancos,543,julio,P,nao')
votacao.append('lei sobre bancos,543,carlos,PBBBB,sim')
votacao.append('lei sobre bancos,543,juliana,PP,sim')
votacao.append('lei das brs,99,joao,PPPP,sim')

assert conta_votos(votacao, 543) == [3, 2]
