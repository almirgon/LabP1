#coding: utf-8
#@Crispiniano 
#Unidade 1: Percentagem de aprovados

print 'Análise da Turma'
print '==='
aprovados = int(raw_input('Número de aprovados? '))
reprovados = int(raw_input('Número de reprovados? '))
print '---'
total = aprovados + reprovados
print 'Total de alunos na turma: {}'.format(total)

porcentagem_1 = float(aprovados * 100)/total
porcentagem_2 = float(reprovados * 100)/total

print 'Aprovados: {} = {:.1f}%'.format(aprovados,porcentagem_1)
print 'Reprovados: {} = {:.1f}%'.format(reprovados,porcentagem_2)

