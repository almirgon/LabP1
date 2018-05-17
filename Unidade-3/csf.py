#coding: utf-8
#Crispiniano
#Unidade 3: CSF

enem = float(raw_input())
creditos = float(raw_input())

if enem < 600:
	if 83.2 < creditos < 374.4:
		print 'Condição ENEM não satisfeita.'
if enem >= 600: 
	if creditos < 83.2 or creditos > 374.4:
		print 'Condição CRÉDITOS não satisfeita.'
if enem < 600:
	if creditos < 83.2 or creditos > 374.4:
		print 'Nenhuma condição satisfeita.'
if enem >= 600:
	if 83.2 < creditos < 374.4:
		print 'Todas as condições satisfeitas.'
		
