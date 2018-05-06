#coding: utf-8
#Crispiniano
#Unidade 2: Dieta

peso = float(raw_input())
tempo = int(raw_input())
calorias = float(raw_input())

calculo1 = (peso * 7700) 
calculo2 = ((tempo * 900) - calorias) + 2000

dieta = calculo1/calculo2

print 'Você precisará de {:.2f} dias de dieta'.format(dieta)
