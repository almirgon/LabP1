#coding: utf-8
#Crispiniano
#Unidade 6: Maioridade Penal Função

def maioridade_penal(nome,idade):
	nome = nome.split()
	idade = idade.split()
	adultos = ''
	for i in range(len(idade)):
		id_nova = int(idade[i])
		if id_nova >= 18:
			adultos += nome[i] + ' '
	adultos = adultos[:-1]
	return adultos 

assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
