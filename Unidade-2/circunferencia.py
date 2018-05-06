#coding: utf-8
#Crispiniano
#Unidade 2: Quadrado na Circunferência

import math 

raio = float(raw_input())

area_circulo = math.pi * (raio**2)

lado = raio * (2**0.5)

area_quadrado = lado ** 2

diferenca = area_circulo - area_quadrado

print 'Área não comum: {:.5f}'.format(diferenca)
