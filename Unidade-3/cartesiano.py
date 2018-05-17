#coding: utf-8
#Crispiniano
#Unidade 3: Cartesiano

x = float(raw_input())
y = float(raw_input())

if x > 0 and y > 0:
	print 'Primeiro quadrante.'
elif x < 0 and y > 0:
	print 'Segundo quadrante.'
elif x < 0 and y < 0:
	print 'Terceiro quadrante.'
elif x > 0 and y < 0:
	print 'Quarto quadrante.'
elif x == 0 and y == 0:
	print 'Centro.'
elif x == 0 or y == 0:
	print 'Sobre eixo.'
