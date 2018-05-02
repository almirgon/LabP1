#coding: utf-8
#@Crispiniano 
#Unidade 1: Calcula Nome

nome = raw_input('Nome? ')
letra = float(raw_input('Letra? R$ '))

calculo = len(nome) * letra 

print 'Orçamento: R$ {}'.format(calculo)
