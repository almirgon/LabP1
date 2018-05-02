#coding: utf-8
#@Crispiniano 
#Unidade 1: Divisão Safra

kg = float(raw_input())
varejo = int(raw_input())
cliente = int(raw_input())

calculo1 = kg/varejo
calculo2 = (kg % varejo)/cliente

print'Clientes no atacado = {:.0f}kg cada.'.format(calculo1)
print'Clientes no varejo = {:.2f}kg cada.'.format(calculo2)
