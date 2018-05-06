#coding: utf-8
#Crispiniano
#Unidade 2: IPTU
area = float(raw_input('Área construída? '))
aliquota = float(raw_input('Alíquota? '))

iptu = (area * aliquota) + 35.00
valor1 = iptu - (iptu * 0.05) 

print 'IPTU: R$ {:.2f}'.format(iptu)

print '\nPagamento:'
print '1. Quota única. R$ {:.2f}'.format(iptu - (iptu * 0.25))
print '2. Em 6 parcelas. Total: R$ {:.2f}'.format(valor1)
print '   6 x R$ {:.2f}'.format(valor1/6)
print '3. Em 10 parcelas. Total: R$ {:.2f}'.format(iptu)
print '   10 x R$ {:.2f}'.format(iptu/10)
