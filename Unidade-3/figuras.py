#coding: utf-8
#Crispiniano
#Unidade 3: Área Figuras

import math 

figura = raw_input()

if figura == 'círculo':
	raio = float(raw_input())
	calculo = math.pi * (raio**2)
	print 'Área do círculo: {:.2f} (cm2)'.format(calculo)
if figura == 'quadrado':
	lado = float(raw_input())
	calculo2 = (lado ** 2)
	print 'Área do quadrado: {:.2f} (cm2)'.format(calculo2)
if figura == 'retângulo':
	base = float(raw_input())
	altura = float(raw_input())
	calculo3 = base * altura 
	print 'Área do retângulo: {:.2f} (cm2)'.format(calculo3)
if figura == 'triângulo':
	base = float(raw_input())
	altura = float(raw_input())
	calculo4 = (base * altura)/2
	print 'Área do triângulo: {:.2f} (cm2)'.format(calculo4)
