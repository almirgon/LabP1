#coding: utf-8
#Crispiniano
#Unidade 2: Área e Perímetro de um Círculo

import math

diametro = float(raw_input())
raio = diametro / 2
area = math.pi * (raio**2)
perimetro = 2 * math.pi * raio
print 'A: {:.5f}'.format(area)
print 'P: {:.5f}'.format(perimetro)
