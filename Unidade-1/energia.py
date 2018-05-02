#coding: utf-8
#@Crispiniano 
#Unidade 1: Consumo Energia

watts = int(raw_input())
tempo = int(raw_input())

segundos = tempo * 60
joules = watts * segundos

calculo = float(joules)/ 3600000

print '{} kWh'.format(calculo)
