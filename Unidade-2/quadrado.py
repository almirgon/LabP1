#coding: utf-8
#Crispiniano
#Unidade 2: Quadrado inscrito na circunferência

import math 

lado = float(raw_input())

r = (lado * (2**0.5))/2

area = (math.pi * ((r)**2))
perimetro = 2 * math.pi * (r)


print 'Perímetro: {:.5f}'.format(perimetro)
print 'Área: {:.5f}'.format(area)
