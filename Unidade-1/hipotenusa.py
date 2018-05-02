#coding: utf-8
#@Crispiniano 
#Unidade 1: Hipotenusa 

cateto1 = float(raw_input('Medida do Cateto 1? '))
cateto2 = float(raw_input('Medida do Cateto 2? '))

calculo = (cateto1**2 + cateto2**2) ** 0.5

print 'Medida da Hipotenusa: {:.2f}'.format(calculo)
