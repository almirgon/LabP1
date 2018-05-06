#coding: utf-8
#Crispiniano
#Unidade 2: Divisão Safra

kg = int(raw_input())
atacado = int(raw_input())
varejo = int(raw_input())

valor1 = kg/atacado 
valor2 = kg % atacado
valor3 = float(valor2)/varejo

print 'Clientes no atacado = {}kg cada.'.format(valor1)
print 'Clientes no varejo = {:.2f}kg cada.'.format(valor3)
