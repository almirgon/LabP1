#coding: utf-8
#Crispiniano
#Unidade 2: Perímetro de Triângulo

import math

x1 = float(raw_input())
y1 = float(raw_input())
x2 = float(raw_input())
y2 = float(raw_input())
x3 = float(raw_input())
y3 = float(raw_input())

distancia1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
distancia3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)

perimetro = distancia1 + distancia2 + distancia3

print "O perímetro é de %.2f" % perimetro
