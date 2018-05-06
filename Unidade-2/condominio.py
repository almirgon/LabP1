#coding: utf-8
#Crispiniano
#Unidade 2: Construção de Condomínio

altura = float(raw_input())
base = float(raw_input())
area_casa = float(raw_input())

area_terreno = altura * base
casas = int(area_terreno / area_casa)

print '{} casa(s) pode(m) ser construída(s) no terreno.'.format(casas)
