#coding: utf-8
#Crispiniano
#Unidade 2: Açudes

capacidade = float(raw_input('capacidade? '))
percentual = float(raw_input('percentual hoje? '))
gasto = float(raw_input('gasto diário? '))

porcentagem = percentual/100
calculo_1 = capacidade * porcentagem
calculo_2 = calculo_1/gasto

print 'volume: {:.2f}'.format(calculo_1)
print 'dias restantes: {}'.format(int(calculo_2))

