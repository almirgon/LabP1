#coding: utf-8
#Crispiniano
#Unidade 6: Filtra Caixas Indisponíveis

def filtra_caixas_indisponiveis(caixas,n):
	for i in range(len(caixas)-1,-1,-1):
		if int(caixas[i]) < n:
			caixas.pop(i)
 
caixas = [0,1,2,3,4,5,6]
filtra_caixas_indisponiveis(caixas,3)
assert caixas == [3,4,5,6]
