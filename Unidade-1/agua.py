#coding: utf-8
#@Crispiniano 
#Unidade 1: Controle de Água

import math

velocidade_de_vazao = float(raw_input())
diametro = float(raw_input())
seccao = (math.pi * diametro**2) / 4
vazao = velocidade_de_vazao * seccao * 1000            
tempo = int(raw_input())
quantidade_de_agua = tempo * vazao
print "Quantidade de água = {} litros.".format(quantidade_de_agua)
