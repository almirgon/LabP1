#coding: utf-8
#@Crispiniano 
#Unidade 1: Peso e IMC

peso = float(raw_input())
altura = float(raw_input())

imc = peso / (altura**2)
print 'IMC atual = {:.2f}'.format(imc)

peso1 = (24.90 - imc) * (altura**2)
print 'Peso a ser ganho/perdido = {:.2f}'.format(peso1)
