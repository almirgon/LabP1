#coding: utf-8
#@Crispiniano 
#Unidade 1: Calcula Moldura

comp = float(raw_input())
largu = float(raw_input())

comp_metro = comp/100
largu_metro = largu/100

calculo = ((comp_metro * 120) + (largu_metro * 120)) * 2

print 'R$ {}'.format(calculo)
