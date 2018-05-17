#coding: utf-8
#Crispiniano
#Unidade 3: Ciclo Trig.

angulo = float(raw_input())

if angulo > 360:
	angulo = angulo % 360

if 0 < angulo < 90:
    print "Quadrante 1"
elif 90 < angulo < 180:
	print "Quadrante 2"
elif 180 < angulo < 270:
    print "Quadrante 3"
elif 270 < angulo < 360:
    print "Quadrante 4"
else:
	print "Sobre eixos"
