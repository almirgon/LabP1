#coding: utf-8
#@Crispiniano 
#Unidade 1: Calcula ingressos do cinema

adultos = int(raw_input())
criancas = int(raw_input())
preco = float(raw_input())

valor = (adultos * preco) + (preco/2) * criancas

print 'Total: R$ {}'.format(valor)
