#coding: utf-8
#Crispiniano
#Unidade 3: Classifica Corredor

km = float(raw_input())
tempo = float(raw_input())

velocidade = km/tempo 

if velocidade < 10:
	print 'Velocidade: {:.1f}km/h. Corredor amador.'.format(velocidade)
if 10 <= velocidade <= 15:
	print 'Velocidade: {:.1f}km/h. Corredor aspirante.'.format(velocidade)
if velocidade > 15:
	print 'Velocidade: {:.1f}km/h. Corredor profissional.'.format(velocidade)

