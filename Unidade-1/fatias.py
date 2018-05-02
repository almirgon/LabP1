#coding: utf-8
#@Crispiniano 
#Unidade 1: Número de Fatias

convidados = int(raw_input())
op1_inteira = 32 / convidados
op1_resto  = 32 % convidados
op2 = 32 / float(convidados)

print 'Opção 1: {} fatias cada, {} de resto'.format(op1_inteira,op1_resto)
print 'Opção 2: {:.2f} fatias cada'.format(op2)
