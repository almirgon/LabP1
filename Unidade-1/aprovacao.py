#coding: utf-8
#Crispiniano
#Unidade 1: Aprovação Unidades

unidade = int(raw_input('Unidade? '))
media = float(raw_input('Média de aprovação na unidade? '))

proxima_unidade = unidade + 1

print '\nO aluno vai para a unidade {} com média {:.1f}.'.format(proxima_unidade,media)
