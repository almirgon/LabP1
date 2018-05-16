#coding: utf-8
#Crispiniano
#Unidade 3: Clássico dos Maiorais

g_campinense = int(raw_input())
g_treze = int(raw_input())

if g_campinense > g_treze:
	print 'Campinense'
elif g_treze > g_campinense:
	print 'Treze'
elif g_campinense == g_treze:
	print 'Empate'
