#coding: utf-8
#Crispiniano
#Unidade 6: Analytics Assembleia

def conta_votos(votacoes,id_votacao):
	votos_sim = 0
	votos_nao = 0
	saida = []
	
	for elemento in votacoes:
		elemento = elemento.split(',')
		if elemento[2] == str(id_votacao):
			if elemento[1] == 'sim':
				votos_sim += 1
			else:
				votos_nao += 1
	saida.append(votos_sim)
	saida.append(votos_nao)
	return saida
	
votacao = []
votacao.append('greve geral,sim,543,joao,servidor')
votacao.append('greve geral,nao,543,marina,servidor')
votacao.append('indicativo de greve,sim,5,joao,professor')
votacao.append('paralisação,nao,543,julio,professor')
votacao.append('paralisação,sim,543,carlos,professor')
votacao.append('paralisação,sim,543,juliana,professor')
votacao.append('lei 1329,sim,99,joao,servidor')

assert conta_votos(votacao, 543) == [3,2]		
