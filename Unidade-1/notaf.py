#coding: utf-8
#@Crispiniano 
#Unidade 1: Nota na final

print '== Estágio 1 =='
peso1 = float(raw_input('Peso? '))
nota1 = float(raw_input('Nota? '))
print '== Estágio 2 =='
peso2 = float(raw_input('Peso? '))
nota2 = float(raw_input('Nota? '))
print '== Estágio 3 =='
peso3 = float(raw_input('Peso? '))
nota3 = float(raw_input('Nota? '))

m_parcial = (peso1*nota1) + (peso2*nota2) + (peso3*nota3)
m_final1 = ((m_parcial * 0.6) - 5.0)/0.4
m_final2 = ((m_parcial * 0.6) - 7.0)/0.4

print '== Resultados =='
print 'Média parcial: {}'.format(m_parcial)
print 'Nota na final, pra média 5.0 = {:.1f}'.format(abs(m_final1))
print 'Nota na final, pra média 7.0 = {:.1f}'.format(abs(m_final2))
