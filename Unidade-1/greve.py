#coding: utf-8
#@Crispiniano 
#Unidade 1: Greve
# Eleição na ADUF

abstencao = int(raw_input())
a_favor = int(raw_input())
contra = int(raw_input())

total = a_favor + contra + abstencao
p1 = float(abstencao * 100)/total
p2 = float(a_favor * 100)/total
p3 = float(contra * 100)/total
print "Resultado da Votação"
print '\n{} abstenções ({:.2f}%)'.format(abstencao, p1)
print '{} a favor ({:.2f}%)'.format(a_favor, p2)
print '{} contra ({:.2f}%)'.format(contra, p3)
