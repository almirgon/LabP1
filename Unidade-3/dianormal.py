#coding: utf-8
#Crispiniano
#Unidade 3: Dia Normal

dia = raw_input()
atendimentos = float(raw_input())

if dia == 'segunda' or dia == 'terça' or dia == 'quarta' or dia == 'quinta' or dia == 'sexta':
	if 40 <= atendimentos <= 60:
		print 'normal'
	else:
		print 'atípico'
elif dia == 'sábado' or dia == 'domingo':
	if atendimentos >= 40:
		print 'normal'
	else:
		print 'atípico'
