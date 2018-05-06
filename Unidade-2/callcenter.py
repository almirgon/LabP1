#coding: utf-8
#Crispiniano
#Unidade 2: Callcenter

atendimento1 = float(raw_input())
atendimento2 = float(raw_input())
atendimento3 = float(raw_input())
atendimento4 = float(raw_input())
atendimento5 = float(raw_input())
atendimento6 = float(raw_input())
atendimento7 = float(raw_input())

total = (atendimento1 + atendimento2 + atendimento3 + atendimento4 + atendimento5 + atendimento6 + atendimento7)
media = (atendimento1 + atendimento2 + atendimento3 + atendimento4 + atendimento5 + atendimento6 + atendimento7)/7

print 'Total: {}'.format(int(total))
print 'Média: {:.2f}'.format(media)

