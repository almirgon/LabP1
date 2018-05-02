#coding: utf-8
#Crispiniano
#Unidade 2: Morangos por Caixa

morango = int(raw_input())

caixa = morango/400
resto = morango % 400

porcentagem = float(resto * 100)/morango

print 'Serão necessárias {} caixa(s) para embalar os morangos.'.format(caixa)
print '{:.1f}% dos morangos serão perdidos.'.format(porcentagem)
