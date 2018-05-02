#coding: utf-8
#@Crispiniano 
#Unidade 1: Imprime Nota Fiscal

nota1 = float(raw_input())
nota2 = float(raw_input())

calculo = (nota1 * 0.6) + (nota2 *0.4)

print 'Média final: {:.1f}'.format(calculo)
