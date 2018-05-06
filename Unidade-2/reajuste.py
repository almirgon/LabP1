#coding: utf-8
#Crispiniano
#Unidade 2: Reajuste do Salário Mínimo

atual = float(raw_input('Valor atual? '))
novo = float(raw_input('Novo valor? '))

diferenca = novo - atual 

p = (diferenca * 100)/atual

print 'Reajuste de {}%'.format(p) 
