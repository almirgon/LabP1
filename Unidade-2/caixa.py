#coding: utf-8
#Crispiniano
#Unidade 2: Caixas de Cerâmica

capacidade = float(raw_input('Capacidade de revestimento? '))

print '\n== Dados do vão a revestir =='
comprimento = float(raw_input('Comprimento? '))
largura = float(raw_input('Largura? '))
altura = float(raw_input('Altura? '))

parede = altura * largura
chao = comprimento * largura
area = (4 * parede) + chao
numero = area/capacidade
print '\n== Resultados =='
print'Área total a revestir: {} m2'.format(area)
print'Número de caixas: {}'.format(int(numero))
