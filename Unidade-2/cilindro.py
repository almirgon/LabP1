#coding: utf-8
#Crispiniano
#Unidade 2: Área do Cilindro

import math

print 'Cálculo da Superfície de um Cilindro'
print '---'
diametro = float(raw_input('Medida do diâmetro? '))
altura = float(raw_input('Medida da altura? '))
print'---'

raio = diametro/2
base = 2 * math.pi * (raio**2)
lateral = 2 * math.pi * raio * altura
area = base + lateral 

print 'Área calculada: {:.2f}'.format(area)
