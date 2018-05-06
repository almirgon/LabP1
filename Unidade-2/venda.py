#coding: utf-8
#Crispiniano
#Unidade 2: Calcula Preço de Venda

custo = float(raw_input())
despesas = float(raw_input())
lucro = float(raw_input())
impostos = float(raw_input())
comissoes = float(raw_input())
descontos = float(raw_input())
encargos = float(raw_input())

percentual1 = custo*(despesas/100)
percentual2 = custo*(lucro/100)

preco = ((custo + percentual1 + percentual2) * 100) / (100-impostos-comissoes-descontos-encargos)

calculo1 = int(preco)
calculo2 = abs(preco - int(preco))
print 'Preço de venda é R$ {:.2f} (R$ {:.2f} + R$ {:.2f})'.format(preco,calculo1,calculo2)
